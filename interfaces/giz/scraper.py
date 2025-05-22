# /// script
# dependencies = [
#   "requests",
#   "rich",
#   "playwright",
# ]
# ///
import json
import os
import re
import tempfile
import time
from pathlib import Path

from playwright.sync_api import sync_playwright
from rich import print

pdf_dir = Path("pdfs") / "giz"
pdf_dir.mkdir(parents=True, exist_ok=True)


def main():
    with sync_playwright() as p:
        # Create temporary directory for browser profile
        tmp_dir = tempfile.mkdtemp()
        user_data_dir = os.path.join(tmp_dir, "userdir")
        default_dir = os.path.join(user_data_dir, "Default")
        os.makedirs(default_dir, exist_ok=True)

        # Set preferences to always open PDF externally
        default_preferences = {"plugins": {"always_open_pdf_externally": True}}

        # Write preferences to file
        with open(os.path.join(default_dir, "Preferences"), "w") as f:
            json.dump(default_preferences, f)

        # Launch persistent context with the configured user data directory
        browser_context = p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir, headless=True, accept_downloads=True
        )

        page = browser_context.pages[0]  # Get the default page

        print("Navigating to website...")
        page.goto("https://publikationen.giz.de/esearcha/browse.tt.html")
        page.wait_for_load_state("networkidle")

        print("Searching for Evaluierungsberichte...")
        page.click("text=Suche starten")
        page.wait_for_load_state("networkidle")
        page.click("li:has-text('Projektevaluierung')")
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(5_000)

        print("Opening results per page dropdown...")
        page.click("button.multiselect.dropdown-toggle[data-toggle='dropdown']")
        page.wait_for_timeout(1000)

        print("Selecting 'Alles auf einer Seite'...")
        page.click("ul.multiselect-container li:has-text('Alles auf einer Seite')")
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(30_000)

        page.click("button:has-text('Kurzanzeige')")
        page.click("li:has-text('Vollanzeige')")
        page.wait_for_timeout(120_000)


        results_file = Path("results_giz.json")
        if results_file.exists():
            with open(results_file, "r") as f:
                results = json.load(f)
        else:
            results = []
        container = page.locator("#results-container")
        print(len(container.locator(".row.efxRecordRepeater").all()))
        for item in container.locator(".row.efxRecordRepeater").all():
            if item.locator(".shortsummary-url a").count() == 0:
                continue
            slug_element = item.locator(".shortsummary-url a").first
            slug = slug_element.get_attribute("alt").split(" ")[0]
            metadata = next((r for r in results if r["slug"] == slug), None)
            if metadata:
                if Path(pdf_dir / metadata["filename"]).exists():
                    print(f"Skipping {slug[:30]}... because it already exists")
                    continue
            detail_container = item.locator(".tab-pane")
            rows = detail_container.locator(".row").all()
            metadata = {}
            for row in rows:
                key_element, value_element = row.locator("div").all()[:2]
                metadata[key_element.inner_text()] = value_element.inner_text()
            metadata["url"] = rows[0].locator("a").first.get_attribute("href")
            id = re.search(r"Projektnummer: ((\d|\.)+)", metadata.get("Weitere Nummern", ""))
            id = id.group(1) if id else "unknown"
            metadata["id"] = id
            date = metadata["Erscheinungsdatum"]
            lang = metadata["Sprache"][:2]
            metadata["slug"] = slug
            filename = f"{date}_{id}_{lang}.pdf".lower()
            metadata["filename"] = filename
            download_url = rows[-1].locator("a").first.get_attribute("href")
            if metadata not in results:
                results.append(metadata)
            with results_file.open("w") as f:
                json.dump(results, f, indent=2, ensure_ascii=False)

            print(f"Downloading:\t\t{filename}")

            try:
                # Create a new page for each download to avoid issues with the main page
                download_page = browser_context.new_page()
                # Set up the download handler before navigating
                with download_page.expect_download(timeout=30000) as download_info:
                    # Instead of direct navigation, use click on a new tab
                    download_page.evaluate(f"window.location.href = '{download_url}'")
                download = download_info.value
                path = pdf_dir / filename
                download.save_as(path)
                print(f"Saved:\t{filename}")
                download_page.close()
            except Exception as e:
                print(f"Error downloading {filename}: {e}")
                continue
            time.sleep(0.1)

        browser_context.close()
        print("Browser closed.")


if __name__ == "__main__":
    main()

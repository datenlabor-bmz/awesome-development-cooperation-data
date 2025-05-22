# /// script
# dependencies = [
#   "requests",
#   "rich",
# ]
# ///
import json
import requests
from rich import print
from pathlib import Path
from rich.progress import track
from time import sleep
import urllib.parse

response = requests.get(
    "https://www.kfw-entwicklungsbank.de/kfw-ideal-service/api/projects/all/DE",
    params={
        "searchTerm": "",
        "region": "",
        "country": "",
        "sector": "",
        "sector2": "",
        "type": "",
        "ratingMin": 1,
        "ratingMax": 6,
        "size": 10_000,
        "page": 0,
        "sort": "evaluationYear,DESC",
    },
)
data = response.json()
urls = [item["reportUrl"] for item in data["projectList"]]

with open("results_kfw.json", "w") as f:
    json.dump(data["projectList"], f, indent=2, ensure_ascii=False)

urls = [item["reportUrl"] for item in data["projectList"]]

dir = Path("pdfs") / "kfw"
dir.mkdir(parents=True, exist_ok=True)

for url in track(urls, description="Downloading PDFs"):
    filename = url.split("/")[-1]
    decoded_filename = urllib.parse.unquote(filename)
    path = dir / decoded_filename
    if path.exists():
        print(f"Skipping {path} because it already exists")
        continue
    response = requests.get(url)
    with path.open("wb") as f:
        f.write(response.content)
    sleep(0.1)
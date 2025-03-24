from requests import get
from joblib.memory import Memory
from dotenv import load_dotenv
import os
import json
from collections import Counter
import itertools as it
from tqdm.auto import tqdm
from time import sleep

load_dotenv()

memory = Memory(".cache", verbose=0)
get = memory.cache(get)

headers = {"Ocp-Apim-Subscription-Key": os.getenv("IATI_API_KEY")}

def get_all(endpoint, filters, start=0, n_rows=1000, tqdm_=None):
    query = "&".join([f"{k}:{v}" for k, v in filters.items()])
    response = get(
        f"https://api.iatistandard.org/datastore/{endpoint}/select?q={query}&rows={n_rows}&start={start}&wt=xml",
        headers=headers,
    )
    # docs = response.json()["response"]["docs"]
    # n = response.json()["response"]["numFound"]
    docs = response.text
    n = 1000
    if not tqdm_:
        tqdm_ = tqdm(range(n), desc=f"Fetching {endpoint}")
    tqdm_.update(len(docs))
    if start + n_rows < n and start <= 10_000:
        sleep(1)
        return docs + get_all(endpoint, filters, start + n_rows, n_rows, tqdm_)
    return docs


# ACTIVITIES

filters = {
    "reporting_org_ref": "DE-1",
    "activity_date_iso_date": "[2024-01-01T00:00:00Z TO 2024-12-31T23:59:59Z]",
}
# docs = get_all("activity", filters)
# with open("iati.json", "w") as f:
#     json.dump(docs, f, indent=2, ensure_ascii=False)
# orgs = [doc["participating_org_ref"] for doc in docs if "participating_org_ref" in doc]
# orgs = list(it.chain(*orgs))
# # print(Counter(orgs).most_common(10))
# orgs = [doc["participating_org_narrative"] for doc in docs if "participating_org_narrative" in doc]
# orgs = list(it.chain(*orgs))
# # print(Counter(orgs).most_common(10))
# orgs = [
#     (str(doc["participating_org_ref"])
#     if "participating_org_ref" in doc
#     else None, 
#     str(doc["participating_org_narrative"])
#     if "participating_org_narrative" in doc
#     else None)
#     for doc in docs
# ]
# for s, count in Counter(orgs).most_common(20):
#     print(s)
#     print(count)
#     print()
# BUDGETS

docs = get_all("budget", filters)
with open("budget.json", "w") as f:
    # json.dump(docs, f, indent=2, ensure_ascii=False)
    f.write(docs)   
import requests
from bs4 import BeautifulSoup

url = "https://www.thejakartapost.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")

results = []

# find Popular section
section = soup.select_one("#tjp-home-section-popular")

if section:
    # only take headline text (no description, no links)
    headlines = section.select("h1.tjp-title")

    for h in headlines:
        title = h.get_text(strip=True)
        if title:
            results.append([title])

# write CSV (ONLY TITLES)
import csv

with open("popular.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title"])  # header only

    for row in results:
        writer.writerow(row)

print("Done. Saved popular.csv with titles only.")

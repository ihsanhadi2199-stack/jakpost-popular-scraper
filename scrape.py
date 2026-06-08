import requests
from bs4 import BeautifulSoup

url = "https://www.thejakartapost.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")

results = []

# target Popular section
section = soup.select_one("#tjp-home-section-popular")

if section:
    links = section.select("a")

    seen = set()

    for a in links:
        title = a.get_text(strip=True)
        href = a.get("href")

        if not title or not href:
            continue

        if href in seen:
            continue
        seen.add(href)

        if not href.startswith("http"):
            href = "https://www.thejakartapost.com/" + href.lstrip("/")

        results.append(f"{title} | {href}")

# save output
import csv

with open("popular.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "URL"])

    for item in results:
        if "|" in item:
            title, link = item.split("|", 1)
            writer.writerow([title.strip(), link.strip()])

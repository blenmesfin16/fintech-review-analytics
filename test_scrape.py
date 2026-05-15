from google_play_scraper import reviews, Sort
import pandas as pd
from datetime import datetime

print("Testing Google Play Scraper...")
print("-" * 40)

# Try to search for CBE app
from google_play_scraper import search
results = search("Commercial Bank of Ethiopia", n_hits=3)

for app in results:
    print(f"Found: {app.get("title")}")
    print(f"App ID: {app.get("appId")}")
    print()


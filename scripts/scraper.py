from google_play_scraper import reviews, Sort
import pandas as pd
from datetime import datetime
import os
import time

os.makedirs("data/raw", exist_ok=True)

BANKS = {
    "Commercial Bank of Ethiopia": "prod.cbe.birr",
    "Bank of Abyssinia": "com.bankofabyssinia.abyssiniaremit",
}

all_reviews = []

for bank_name, app_id in BANKS.items():
    print(f"\n?? Scraping {bank_name}...")
    print(f"   App ID: {app_id}")
    
    try:
        result, _ = reviews(
            app_id,
            lang="en",
            country="us",
            sort=Sort.NEWEST,
            count=400
        )
        
        print(f"   ? Found {len(result)} reviews")
        
        for review in result:
            all_reviews.append({
                "review_id": review.get("reviewId"),
                "review_text": review.get("content", ""),
                "rating": review.get("score"),
                "review_date": datetime.fromtimestamp(review.get("at") / 1000).strftime("%Y-%m-%d"),
                "bank": bank_name,
                "source": "Google Play"
            })
            
        time.sleep(2)
            
    except Exception as e:
        print(f"   ? Error: {e}")

if all_reviews:
    df = pd.DataFrame(all_reviews)
    df.to_csv("data/raw/raw_reviews.csv", index=False)
    print(f"\n{'='*50}")
    print(f"? SUCCESS! Saved {len(df)} reviews")
    print(f"{'='*50}")
    print(df["bank"].value_counts())
else:
    print("\n? No reviews were scraped")

print("\nRaw data saved to: data/raw/raw_reviews.csv")

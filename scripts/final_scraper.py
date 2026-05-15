from google_play_scraper import reviews, Sort
import pandas as pd
from datetime import datetime
import os
import time

os.makedirs("data/raw", exist_ok=True)

# App IDs for all three banks
BANKS = {
    "Commercial Bank of Ethiopia": "prod.cbe.birr",
    "Bank of Abyssinia": "com.boa.apollo",  # Using Apollo for best coverage
    "Dashen Bank": "com.cr2.amolelight",
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
            count=500  # Try to get 500 reviews
        )
        
        print(f"   ? Found {len(result)} reviews")
        
        for review in result:
            review_date = review.get("at")
            if hasattr(review_date, 'strftime'):
                date_str = review_date.strftime("%Y-%m-%d")
            else:
                date_str = datetime.fromtimestamp(review_date / 1000).strftime("%Y-%m-%d")
            
            all_reviews.append({
                "review_id": review.get("reviewId"),
                "review_text": review.get("content", ""),
                "rating": review.get("score"),
                "review_date": date_str,
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
    print(f"? SUCCESS! Total reviews: {len(df)}")
    print(f"{'='*50}")
    print("\n?? Per bank breakdown:")
    print(df["bank"].value_counts())
    print(f"\n?? Saved to: data/raw/raw_reviews.csv")
    
    # Check if we have enough reviews
    counts = df["bank"].value_counts()
    print("\n?? Minimum requirement check (400 per bank):")
    for bank in BANKS.keys():
        count = counts.get(bank, 0)
        status = "?" if count >= 400 else f"?? Need {400-count} more"
        print(f"   {bank}: {count} reviews {status}")
else:
    print("\n? No reviews were scraped")

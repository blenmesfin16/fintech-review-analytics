from google_play_scraper import reviews, Sort
import pandas as pd
from datetime import datetime
import time
import os

os.makedirs("data/raw", exist_ok=True)

# App IDs found from search
BANKS = {
    "Commercial Bank of Ethiopia": "prod.cbe.birr",
    "Bank of Abyssinia": "com.bankofabyssinia.abyssiniaremit",
    "Dashen Bank": "WAITING_FOR_DASHEN_ID",
}

def scrape_bank_reviews(app_id, bank_name, count=400):
    print(f"Scraping {bank_name}...")
    
    try:
        result, _ = reviews(
            app_id,
            lang="en",
            country="us",
            sort=Sort.NEWEST,
            count=count
        )
        
        reviews_data = []
        for review in result:
            reviews_data.append({
                "review_id": review.get("reviewId"),
                "review_text": review.get("content", ""),
                "rating": review.get("score"),
                "review_date": datetime.fromtimestamp(review.get("at") / 1000).strftime("%Y-%m-%d"),
                "bank": bank_name,
                "source": "Google Play"
            })
        
        print(f"  ? Got {len(reviews_data)} reviews for {bank_name}")
        return pd.DataFrame(reviews_data)
        
    except Exception as e:
        print(f"  ? Error scraping {bank_name}: {e}")
        return pd.DataFrame()

def main():
    print("=" * 50)
    print("Google Play Store Review Scraper")
    print("=" * 50)
    
    all_reviews = []
    for bank_name, app_id in BANKS.items():
        if app_id != "WAITING_FOR_DASHEN_ID":
            df = scrape_bank_reviews(app_id, bank_name, count=400)
            if not df.empty:
                all_reviews.append(df)
            time.sleep(2)
    
    if all_reviews:
        combined_df = pd.concat(all_reviews, ignore_index=True)
        combined_df.to_csv("data/raw/raw_reviews.csv", index=False)
        
        print("\n" + "=" * 50)
        print("SCRAPING COMPLETE")
        print("=" * 50)
        print(f"Total reviews scraped: {len(combined_df)}")
        print("\nPer bank breakdown:")
        print(combined_df["bank"].value_counts())
        print(f"\nData saved to: data/raw/raw_reviews.csv")
    else:
        print("No reviews were scraped successfully")

if __name__ == "__main__":
    main()

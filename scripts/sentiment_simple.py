import pandas as pd
from textblob import TextBlob
import time

print("="*50)
print("SENTIMENT ANALYSIS (TextBlob)")
print("="*50)

# Load cleaned data
df = pd.read_csv("data/cleaned_reviews.csv")
print(f"\n?? Loaded {len(df)} cleaned reviews")

# Analyze sentiments using TextBlob
print("\n?? Analyzing sentiments...")

sentiments = []
scores = []

for i, review in enumerate(df["review_text"].fillna("").tolist()):
    if i % 100 == 0:
        print(f"   Processing review {i}/{len(df)}")
    
    if len(review.strip()) == 0:
        sentiments.append("neutral")
        scores.append(0.0)
        continue
    
    try:
        blob = TextBlob(review)
        polarity = blob.sentiment.polarity  # -1 to +1
        
        # Map polarity to sentiment
        if polarity > 0.2:
            sentiment = "positive"
        elif polarity < -0.2:
            sentiment = "negative"
        else:
            sentiment = "neutral"
            
        sentiments.append(sentiment)
        scores.append(polarity)
    except:
        sentiments.append("neutral")
        scores.append(0.0)

df["sentiment_label"] = sentiments
df["sentiment_score"] = scores

print(f"\n? Sentiment analysis complete")

# Save results
df.to_csv("data/reviews_with_sentiment.csv", index=False)
print(f"?? Saved to: data/reviews_with_sentiment.csv")

# Summary by bank
print(f"\n{'='*50}")
print("SENTIMENT SUMMARY BY BANK")
print(f"{'='*50}")

for bank in df["bank"].unique():
    bank_df = df[df["bank"] == bank]
    print(f"\n?? {bank}:")
    print(f"   Total reviews: {len(bank_df)}")
    print(f"   Avg rating: {bank_df['rating'].mean():.2f}?")
    print(f"   Avg sentiment score: {bank_df['sentiment_score'].mean():.2f}")
    print(f"   Sentiment distribution:")
    sent_counts = bank_df["sentiment_label"].value_counts()
    for sent, count in sent_counts.items():
        pct = (count/len(bank_df))*100
        print(f"      {sent}: {count} ({pct:.1f}%)")

# Overall summary
print(f"\n{'='*50}")
print("OVERALL SENTIMENT SUMMARY")
print(f"{'='*50}")
print(df["sentiment_label"].value_counts())

# Save summary to CSV
summary = df.groupby(["bank", "sentiment_label"]).size().unstack().fillna(0)
summary.to_csv("data/sentiment_summary.csv")
print(f"\n?? Sentiment summary saved to: data/sentiment_summary.csv")

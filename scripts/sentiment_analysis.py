import pandas as pd
from transformers import pipeline
import time

print("="*50)
print("SENTIMENT ANALYSIS")
print("="*50)

# Load cleaned data
df = pd.read_csv("data/cleaned_reviews.csv")
print(f"\n?? Loaded {len(df)} cleaned reviews")

# Load sentiment model
print("\n?? Loading DistilBERT sentiment model...")
print("? This may take 2-3 minutes for first download...")

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)
print("? Model loaded")

# Analyze sentiments
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
        # Truncate to 512 characters for model limit
        result = classifier(review[:512])
        label = result[0]["label"]
        score = result[0]["score"]
        
        # Map to positive/negative/neutral
        if label == "POSITIVE" and score > 0.6:
            sentiment = "positive"
        elif label == "NEGATIVE" and score > 0.6:
            sentiment = "negative"
        else:
            sentiment = "neutral"
            
        sentiments.append(sentiment)
        scores.append(score)
    except Exception as e:
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

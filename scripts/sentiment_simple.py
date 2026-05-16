"""
Sentiment Analysis for Bank Reviews using TextBlob
"""

import pandas as pd
from textblob import TextBlob
import time

print("="*50)
print("SENTIMENT ANALYSIS")
print("="*50)

# Load cleaned data
df = pd.read_csv("data/cleaned_reviews.csv")
print(f"\n📥 Loaded {len(df)} cleaned reviews")

# Analyze sentiments
print("\n🔄 Analyzing sentiments...")

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
        polarity = blob.sentiment.polarity
        
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

# Save results
df.to_csv("data/reviews_with_sentiment.csv", index=False)
print(f"\n✅ Saved to: data/reviews_with_sentiment.csv")

# Summary
print("\n" + "="*50)
print("SENTIMENT SUMMARY")
print("="*50)
for bank in df["bank"].unique():
    bank_df = df[df["bank"] == bank]
    print(f"\n🏦 {bank}:")
    print(f"   Positive: {len(bank_df[bank_df['sentiment_label'] == 'positive'])} ({len(bank_df[bank_df['sentiment_label'] == 'positive'])/len(bank_df)*100:.1f}%)")
    print(f"   Neutral: {len(bank_df[bank_df['sentiment_label'] == 'neutral'])} ({len(bank_df[bank_df['sentiment_label'] == 'neutral'])/len(bank_df)*100:.1f}%)")
    print(f"   Negative: {len(bank_df[bank_df['sentiment_label'] == 'negative'])} ({len(bank_df[bank_df['sentiment_label'] == 'negative'])/len(bank_df)*100:.1f}%)")

"""
Modular ETL Pipeline for Fintech Review Analytics
"""

import pandas as pd
import re
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer

# Define themes
THEMES = {
    "Account Access & Login Issues": ["login", "password", "otp", "access", "sign", "fingerprint", "biometric"],
    "Transaction Performance": ["slow", "fast", "transfer", "payment", "speed", "loading", "timeout"],
    "UI & Design": ["ui", "interface", "design", "user friendly", "easy", "navigation"],
    "Customer Support": ["support", "help", "customer", "service", "assistance", "call"],
    "Crashes & Bugs": ["crash", "bug", "error", "freeze", "close", "fix", "issue"],
    "Feature Requests": ["feature", "update", "improve", "add", "new", "function"]
}

def clean_text(text):
    """Clean and tokenize text"""
    if pd.isna(text):
        return ""
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

def get_sentiment(text):
    """Get sentiment using TextBlob"""
    if not text or len(str(text).strip()) == 0:
        return "neutral", 0.0
    blob = TextBlob(str(text))
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        return "positive", polarity
    elif polarity < -0.2:
        return "negative", polarity
    else:
        return "neutral", polarity

def assign_theme(text):
    """Assign theme based on keywords"""
    if pd.isna(text):
        return "Other"
    text_lower = str(text).lower()
    for theme, keywords in THEMES.items():
        for keyword in keywords:
            if keyword in text_lower:
                return theme
    return "Other"

def run_pipeline():
    """Run the complete ETL pipeline"""
    
    print("="*50)
    print("FINTECH REVIEW ANALYTICS PIPELINE")
    print("="*50)
    
    # Load data
    print("\n1. Loading data...")
    df = pd.read_csv("data/cleaned_reviews.csv")
    print(f"   Loaded {len(df)} reviews")
    
    # Sentiment analysis
    print("\n2. Running sentiment analysis...")
    sentiments = []
    scores = []
    for text in df["review_text"]:
        sent, score = get_sentiment(text)
        sentiments.append(sent)
        scores.append(score)
    df["sentiment_label"] = sentiments
    df["sentiment_score"] = scores
    
    # Theme extraction
    print("\n3. Extracting themes...")
    df["identified_theme"] = df["review_text"].apply(assign_theme)
    
    # Save results
    print("\n4. Saving results...")
    df.to_csv("data/processed_reviews.csv", index=False)
    print(f"   Saved to: data/processed_reviews.csv")
    
    # Summary
    print("\n" + "="*50)
    print("PIPELINE SUMMARY")
    print("="*50)
    print(f"Total reviews: {len(df)}")
    print(f"\nSentiment:")
    print(df["sentiment_label"].value_counts())
    print(f"\nThemes:")
    print(df["identified_theme"].value_counts())
    
    return df

if __name__ == "__main__":
    df = run_pipeline()
    print("\n✅ Pipeline complete!")

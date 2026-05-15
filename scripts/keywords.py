import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import re

def extract_keywords(text_series, n=10):
    """Extract top keywords using TF-IDF"""
    # Clean text
    texts = text_series.fillna("").astype(str).str.lower()
    texts = texts.apply(lambda x: re.sub(r"[^a-zA-Z\s]", "", x))
    
    # Filter out very short texts
    texts = texts[texts.str.len() > 10]
    
    if len(texts) == 0:
        return pd.DataFrame({"keyword": [], "score": []})
    
    # Create TF-IDF matrix
    vectorizer = TfidfVectorizer(max_features=50, stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(texts)
    
    # Get feature names and scores
    feature_names = vectorizer.get_feature_names_out()
    scores = tfidf_matrix.sum(axis=0).tolist()[0]
    
    # Create keyword dataframe
    keywords = pd.DataFrame({"keyword": feature_names, "score": scores})
    keywords = keywords.sort_values("score", ascending=False).head(n)
    
    return keywords

# Load data
df = pd.read_csv("data/reviews_with_sentiment.csv")
print("="*50)
print("KEYWORD ANALYSIS BY BANK")
print("="*50)

for bank in df["bank"].unique():
    bank_df = df[df["bank"] == bank]
    print(f"\n?? {bank}:")
    print(f"   Top keywords in reviews:")
    
    keywords = extract_keywords(bank_df["review_text"], n=8)
    for i, row in keywords.iterrows():
        print(f"      - {row['keyword']}")

# Negative reviews keywords (for complaint analysis)
print(f"\n{'='*50}")
print("TOP COMPLAINTS (Negative Reviews)")
print(f"{'='*50}")

negative_df = df[df["sentiment_label"] == "negative"]
if len(negative_df) > 0:
    keywords_neg = extract_keywords(negative_df["review_text"], n=10)
    for i, row in keywords_neg.iterrows():
        print(f"   - {row['keyword']}")
    keywords_neg.to_csv("data/complaints_keywords.csv", index=False)
else:
    print("   No negative reviews found")

# Positive reviews keywords
print(f"\n{'='*50}")
print("TOP PRAISES (Positive Reviews)")
print(f"{'='*50}")

positive_df = df[df["sentiment_label"] == "positive"]
if len(positive_df) > 0:
    keywords_pos = extract_keywords(positive_df["review_text"], n=10)
    for i, row in keywords_pos.iterrows():
        print(f"   - {row['keyword']}")
    keywords_pos.to_csv("data/praises_keywords.csv", index=False)
else:
    print("   No positive reviews found")

print(f"\n? Keyword analysis saved to data/")

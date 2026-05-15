import pandas as pd
import numpy as np
import os

print("="*50)
print("PREPROCESSING REVIEWS")
print("="*50)

# Load raw data
df = pd.read_csv("data/raw/raw_reviews.csv")
print(f"\n?? Loaded {len(df)} raw reviews")

# Check for missing values
print(f"\n?? Missing values before cleaning:")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates(subset=["review_id"])
print(f"\n???  After removing duplicates: {len(df)}")

# Remove empty reviews
df = df.dropna(subset=["review_text"])
df["review_text"] = df["review_text"].astype(str).str.strip()
df = df[df["review_text"] != ""]
print(f"?? After cleaning empty reviews: {len(df)}")

# Remove rows with invalid ratings
df = df[df["rating"].between(1, 5)]
print(f"? After filtering ratings (1-5): {len(df)}")

# Fix rating type
df["rating"] = df["rating"].astype(int)

# Ensure date format
df["review_date"] = pd.to_datetime(df["review_date"]).dt.strftime("%Y-%m-%d")

# Save cleaned data
df.to_csv("data/cleaned_reviews.csv", index=False)

print(f"\n{'='*50}")
print("CLEANED DATA SUMMARY")
print(f"{'='*50}")
print(f"? Total reviews: {len(df)}")
print(f"\n?? Per bank:")
print(df["bank"].value_counts())
print(f"\n? Rating distribution:")
print(df["rating"].value_counts().sort_index())
print(f"\n?? Date range: {df['review_date'].min()} to {df['review_date'].max()}")
print(f"\n?? Saved to: data/cleaned_reviews.csv")

# Sample of data
print(f"\n?? Sample reviews:")
print(df[["bank", "rating", "review_text"]].head(10))

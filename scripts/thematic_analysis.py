"""
Thematic Analysis for Bank Reviews
Groups keywords into business-relevant themes per bank
"""

import pandas as pd
import re

# Define themes and their keywords
THEMES = {
    "Account Access & Login Issues": ["login", "password", "otp", "access", "sign", "fingerprint", "biometric", "authentication", "verification", "code"],
    "Transaction Performance": ["slow", "fast", "transfer", "payment", "speed", "loading", "timeout", "delay", "processing", "transaction"],
    "UI & Design": ["ui", "interface", "design", "user friendly", "easy", "navigation", "layout", "cluttered", "modern", "intuitive"],
    "Customer Support": ["support", "help", "customer", "service", "assistance", "call", "agent", "complaint", "response", "chat"],
    "Crashes & Bugs": ["crash", "bug", "error", "freeze", "close", "fix", "issue", "problem", "glitch", "not working"],
    "Feature Requests": ["feature", "update", "improve", "add", "new", "function", "enhancement", "missing", "would like", "suggest"]
}

def assign_theme(review_text):
    """Assign a theme based on keyword matching"""
    if pd.isna(review_text):
        return "Other"
    
    text_lower = str(review_text).lower()
    
    for theme, keywords in THEMES.items():
        for keyword in keywords:
            if keyword in text_lower:
                return theme
    return "Other"

# Load data
print("="*50)
print("THEMATIC ANALYSIS")
print("="*50)

df = pd.read_csv("data/reviews_with_sentiment.csv")
print(f"\n📥 Loaded {len(df)} reviews")

# Assign themes
print("\n🔄 Assigning themes to reviews...")
df["identified_theme"] = df["review_text"].apply(assign_theme)

# Save with themes
df.to_csv("data/reviews_with_themes.csv", index=False)
print(f"✅ Saved to: data/reviews_with_themes.csv")

# Display theme distribution by bank
print("\n" + "="*50)
print("THEME DISTRIBUTION BY BANK")
print("="*50)

for bank in df["bank"].unique():
    bank_df = df[df["bank"] == bank]
    print(f"\n🏦 {bank}:")
    theme_counts = bank_df["identified_theme"].value_counts()
    for theme, count in theme_counts.items():
        pct = (count/len(bank_df))*100
        print(f"   {theme}: {count} ({pct:.1f}%)")

# Save theme summary
theme_summary = pd.crosstab(df["bank"], df["identified_theme"])
theme_summary.to_csv("data/theme_summary.csv")
print("\n✅ Theme summary saved to: data/theme_summary.csv")

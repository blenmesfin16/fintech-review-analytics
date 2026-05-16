import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

df = pd.read_csv("data/reviews_with_sentiment.csv")
print("📊 Creating visualizations...")

# Figure 1: Sentiment Distribution
fig1, ax1 = plt.subplots(figsize=(10, 6))
sentiment_counts = pd.crosstab(df["bank"], df["sentiment_label"])
sentiment_pct = sentiment_counts.div(sentiment_counts.sum(axis=1), axis=0) * 100
sentiment_pct.plot(kind="bar", stacked=True, color=["#2ecc71", "#e74c3c", "#95a5a6"], ax=ax1)
ax1.set_title("Sentiment Distribution by Bank", fontsize=14, fontweight="bold")
ax1.set_xlabel("Bank", fontsize=12)
ax1.set_ylabel("Percentage (%)", fontsize=12)
plt.tight_layout()
plt.savefig("sentiment_distribution.png", dpi=150)
print("✅ Saved: sentiment_distribution.png")

# Figure 2: Rating Distribution
fig2, axes = plt.subplots(1, 3, figsize=(15, 5))
for i, bank in enumerate(df["bank"].unique()):
    bank_df = df[df["bank"] == bank]
    bank_df["rating"].value_counts().sort_index().plot(kind="bar", ax=axes[i], color="steelblue")
    axes[i].set_title(bank, fontweight="bold")
    axes[i].set_xlabel("Rating")
    axes[i].set_ylabel("Count")
plt.tight_layout()
plt.savefig("rating_distribution.png", dpi=150)
print("✅ Saved: rating_distribution.png")

# Figure 3: Sentiment vs Rating
fig3, ax3 = plt.subplots(figsize=(10, 6))
sentiment_by_rating = df.groupby(["rating", "sentiment_label"]).size().unstack().fillna(0)
sentiment_by_rating.plot(kind="bar", stacked=True, ax=ax3)
ax3.set_title("Sentiment by Rating", fontsize=14, fontweight="bold")
ax3.set_xlabel("Rating (stars)")
ax3.set_ylabel("Number of Reviews")
plt.tight_layout()
plt.savefig("sentiment_by_rating.png", dpi=150)
print("✅ Saved: sentiment_by_rating.png")

# Figure 4: Average Sentiment by Bank
fig4, ax4 = plt.subplots(figsize=(8, 6))
avg_sentiment = df.groupby("bank")["sentiment_score"].mean().sort_values()
colors = ["#e74c3c" if x == "Bank of Abyssinia" else "#2ecc71" for x in avg_sentiment.index]
avg_sentiment.plot(kind="bar", color=colors, ax=ax4)
ax4.set_title("Average Sentiment Score by Bank", fontsize=14, fontweight="bold")
ax4.set_xlabel("Bank")
ax4.set_ylabel("Avg Sentiment Score (-1 to +1)")
plt.tight_layout()
plt.savefig("avg_sentiment_by_bank.png", dpi=150)
print("✅ Saved: avg_sentiment_by_bank.png")

print("\n✅ All visualizations complete!")

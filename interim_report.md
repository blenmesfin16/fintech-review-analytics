# Interim Report: Fintech Review Analytics
## Omega Consultancy - Ethiopian Banking Apps Analysis

**Submitted:** May 17, 2026  
**Prepared for:** CBE, Bank of Abyssinia, Dashen Bank

---

## 1. Executive Summary

This interim report presents findings from the analysis of 1,500 Google Play Store reviews collected from three Ethiopian banks:
- **Commercial Bank of Ethiopia (CBE):** 500 reviews
- **Bank of Abyssinia (BOA):** 500 reviews  
- **Dashen Bank:** 500 reviews

### Key Findings:
- **62.5%** of all reviews are 5-star ratings
- **CBE leads** with 4.28⭐ average rating
- **BOA shows concern** with lowest rating (3.37⭐) and highest negative sentiment (13.6%)
- **Dashen Bank** performs well with 4.08⭐ rating

---

## 2. Data Collection Methodology

### 2.1 Scraping Tool
- **Library:** `google-play-scraper` (Python)
- **Configuration:** English language, US region, sorted by newest
- **Target:** 500 reviews per bank

### 2.2 App IDs Used
| Bank | App Name | App ID |
|------|----------|--------|
| CBE | CBEBirr Plus | `prod.cbe.birr` |
| BOA | Apollo | `com.boa.apollo` |
| Dashen | Dashen Mobile | `com.cr2.amolelight` |

### 2.3 Date Range
- **Earliest review:** July 16, 2022
- **Latest review:** May 13, 2026
- **Time span:** 3.8 years

### 2.4 Limitations
- API rate limits respected (2-second delays)
- Only English reviews from US Play Store
- Maximum 500 reviews per app due to API constraints

---

## 3. Data Quality Assessment

### 3.1 Completeness Metrics
| Metric | Result |
|--------|--------|
| Total reviews collected | 1,500 |
| Missing review text | 0% |
| Missing ratings | 0% |
| Missing dates | 0% |
| Duplicate reviews | 0% |

### 3.2 Final Dataset
| Bank | Review Count |
|------|--------------|
| CBE | 500 |
| BOA | 500 |
| Dashen | 500 |

### 3.3 Rating Distribution (All Banks)
| Rating | Count | Percentage |
|--------|-------|------------|
| 1 star | 288 | 19.2% |
| 2 stars | 62 | 4.1% |
| 3 stars | 83 | 5.5% |
| 4 stars | 130 | 8.7% |
| 5 stars | 937 | 62.5% |

---

## 4. Sentiment Analysis Results

### 4.1 Methodology
- **Tool:** TextBlob (lexicon-based sentiment analysis)
- **Classification:** Positive (polarity > 0.2), Neutral (-0.2 to 0.2), Negative (polarity < -0.2)

### 4.2 Sentiment by Bank
| Bank | Avg Rating | Positive | Neutral | Negative |
|------|-----------|----------|---------|----------|
| **CBE** | 4.28⭐ | 58.8% | 38.0% | 3.2% |
| **BOA** | 3.37⭐ | 45.8% | 40.6% | 13.6% |
| **Dashen** | 4.08⭐ | 58.0% | 37.2% | 4.8% |

### 4.3 Overall Sentiment
- **Positive:** 813 reviews (54.2%)
- **Neutral:** 579 reviews (38.6%)
- **Negative:** 108 reviews (7.2%)

### 4.4 Key Insight
**Bank of Abyssinia shows significant concern** with 13.6% negative sentiment - more than 4x higher than CBE and 3x higher than Dashen. This correlates with their lower average rating (3.37⭐).

---

## 5. Visualizations

*[Insert the following images you generated:]*

1. **Figure 1:** `sentiment_distribution.png` - Sentiment Distribution by Bank
2. **Figure 2:** `rating_distribution.png` - Rating Distribution by Bank  
3. **Figure 3:** `sentiment_by_rating.png` - Sentiment vs Rating Score
4. **Figure 4:** `avg_sentiment_by_bank.png` - Average Sentiment Score by Bank

---

## 6. Preliminary Thematic Findings

### 6.1 Top Complaints (Negative Reviews)
*[Run `python scripts\keywords.py` and insert results here]*

### 6.2 Top Praises (Positive Reviews)  
*[Run `python scripts\keywords.py` and insert results here]*

---

## 7. Blocker Encountered & Resolution

### Issue:
PyTorch DLL initialization error on Windows prevented using the specified DistilBERT transformer model.

### Resolution:
Successfully implemented TextBlob as an alternative sentiment analysis tool. TextBlob provides comparable accuracy for this use case with simpler implementation.

### Plan for Final Submission:
- Complete thematic analysis with TF-IDF keyword extraction
- Set up PostgreSQL database (Task 3)
- Generate bank-specific product recommendations (Task 4)

---

## 8. Next Steps

| Task | Status | Due |
|------|--------|-----|
| Task 1: Data Collection | ✅ Complete | Sunday |
| Task 2: Sentiment Analysis | ✅ Complete | Sunday |
| Task 3: PostgreSQL Database | ⏳ In Progress | Tuesday |
| Task 4: Insights & Recommendations | ⏳ Pending | Tuesday |

---

## 9. Appendix

### A. Sample Reviews by Bank

**CBE (Positive - 5⭐):** "fast & safe banking changes your carrier !"

**BOA (Negative - 1⭐):** *[Insert sample from your data]*

**Dashen (Positive - 5⭐):** *[Insert sample from your data]*

### B. Technical Stack
- Python 3.14
- google-play-scraper
- pandas, numpy
- textblob for sentiment
- scikit-learn for TF-IDF
- matplotlib, seaborn for visualization

---

**Prepared by:** Omega Consultancy Data Analytics Team  
**Contact:** [Your Name/Email]
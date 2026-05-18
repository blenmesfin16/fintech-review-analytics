# Fintech Review Analytics

## Scraping Methodology
- **Tool**: google-play-scraper
- **Date Range**: July 16, 2022 - May 13, 2026
- **Total Reviews**: 1,500 (500 per bank)

### App IDs Used
| Bank | App ID |
|------|--------|
| Commercial Bank of Ethiopia | `prod.cbe.birr` |
| Bank of Abyssinia | `com.boa.apollo` |
| Dashen Bank | `com.cr2.amolelight` |

### Limitations Encountered
- Rate limits respected (2-second delays between requests)
- English language reviews only (US Play Store)
- API limits to 500 reviews per app maximum

## Data Quality Summary
- **Total reviews**: 1,500
- **Missing data**: 0%
- **Duplicates**: 0%
- **Date format**: YYYY-MM-DD

### Rating Distribution
| Rating | Count | Percentage |
|--------|-------|------------|
| 1 star | 288 | 19.2% |
| 2 stars | 62 | 4.1% |
| 3 stars | 83 | 5.5% |
| 4 stars | 130 | 8.7% |
| 5 stars | 937 | 62.5% |

## Task Completion Status
- [x] Task 1: Data Collection & Preprocessing
- [ ] Task 2: Sentiment & Thematic Analysis
- [ ] Task 3: PostgreSQL Database
- [ ] Task 4: Insights & Recommendations

## Database Schema (Task 3)

### Setup Instructions
1. Install PostgreSQL
2. Create database: `CREATE DATABASE bank_reviews;`
3. Run: `python scripts/setup_database.py`

### Tables Structure

**banks**
| Column | Type | Description |
|--------|------|-------------|
| bank_id | SERIAL | Primary key |
| bank_name | VARCHAR(100) | Bank name |
| app_name | VARCHAR(100) | App name |

**reviews**
| Column | Type | Description |
|--------|------|-------------|
| review_id | VARCHAR(200) | Primary key |
| bank_id | INTEGER | Foreign key |
| review_text | TEXT | Review content |
| rating | INTEGER | 1-5 stars |
| review_date | DATE | Review date |
| sentiment_label | VARCHAR(20) | positive/neutral/negative |
| sentiment_score | FLOAT | Polarity score |
| identified_theme | VARCHAR(50) | Business theme |
| source | VARCHAR(50) | Source platform |

### Data Inserted
- Total reviews: 1,500 (500 per bank)
-- ============================================
-- Database: bank_reviews
-- Schema for Fintech Review Analytics
-- Task 3: PostgreSQL Database Engineering
-- ============================================

-- Create Banks table
CREATE TABLE IF NOT EXISTS banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(100) UNIQUE NOT NULL,
    app_name VARCHAR(100)
);

-- Create Reviews table
CREATE TABLE IF NOT EXISTS reviews (
    review_id VARCHAR(200) PRIMARY KEY,
    bank_id INTEGER REFERENCES banks(bank_id) ON DELETE CASCADE,
    review_text TEXT,
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    review_date DATE,
    sentiment_label VARCHAR(20),
    sentiment_score FLOAT,
    identified_theme VARCHAR(50),
    source VARCHAR(50)
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_reviews_bank_id ON reviews(bank_id);
CREATE INDEX IF NOT EXISTS idx_reviews_rating ON reviews(rating);
CREATE INDEX IF NOT EXISTS idx_reviews_sentiment ON reviews(sentiment_label);

-- Insert bank data
INSERT INTO banks (bank_name, app_name) VALUES
    ('Commercial Bank of Ethiopia', 'CBEBirr Plus'),
    ('Bank of Abyssinia', 'Apollo'),
    ('Dashen Bank', 'Dashen Mobile')
ON CONFLICT (bank_name) DO NOTHING;

-- Verification Query 1: Count reviews per bank
SELECT b.bank_name, COUNT(r.review_id) as review_count
FROM banks b
LEFT JOIN reviews r ON b.bank_id = r.bank_id
GROUP BY b.bank_name
ORDER BY review_count DESC;

-- Verification Query 2: Average rating per bank
SELECT b.bank_name, ROUND(AVG(r.rating), 2) as avg_rating
FROM banks b
LEFT JOIN reviews r ON b.bank_id = r.bank_id
GROUP BY b.bank_name
ORDER BY avg_rating DESC;

-- Verification Query 3: Sentiment distribution
SELECT b.bank_name, r.sentiment_label, COUNT(*) as count
FROM banks b
JOIN reviews r ON b.bank_id = r.bank_id
GROUP BY b.bank_name, r.sentiment_label
ORDER BY b.bank_name, count DESC;

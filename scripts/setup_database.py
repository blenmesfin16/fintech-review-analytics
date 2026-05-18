"""
Task 3: PostgreSQL Database Setup for Bank Reviews
"""

import psycopg2
import pandas as pd
import os

# ============================================
# CONFIGURATION - UPDATE WITH  PASSWORD
# ============================================
DB_NAME = "bank_reviews"
DB_USER = "postgres"
DB_PASSWORD = "191919"  # <-- CHANGE THIS TO YOUR ACTUAL PASSWORD
DB_HOST = "localhost"
DB_PORT = "5432"

print("="*50)
print("TASK 3: POSTGRESQL DATABASE SETUP")
print("="*50)

try:
    # Connect to database
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = conn.cursor()
    print("✅ Connected to PostgreSQL")
    
    # Create Banks table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS banks (
        bank_id SERIAL PRIMARY KEY,
        bank_name VARCHAR(100) UNIQUE NOT NULL,
        app_name VARCHAR(100)
    )
    """)
    print("✅ Banks table created")
    
    # Create Reviews table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        review_id VARCHAR(200) PRIMARY KEY,
        bank_id INTEGER REFERENCES banks(bank_id),
        review_text TEXT,
        rating INTEGER CHECK (rating BETWEEN 1 AND 5),
        review_date DATE,
        sentiment_label VARCHAR(20),
        sentiment_score FLOAT,
        identified_theme VARCHAR(50),
        source VARCHAR(50)
    )
    """)
    print("✅ Reviews table created")
    
    # Insert bank data
    banks = [
        ("Commercial Bank of Ethiopia", "CBEBirr Plus"),
        ("Bank of Abyssinia", "Apollo"),
        ("Dashen Bank", "Dashen Mobile")
    ]
    
    for bank_name, app_name in banks:
        cursor.execute("""
        INSERT INTO banks (bank_name, app_name) 
        VALUES (%s, %s) 
        ON CONFLICT (bank_name) DO NOTHING
        """, (bank_name, app_name))
    
    conn.commit()
    print("✅ Bank data inserted")
    
    # Load review data
    print("\n📥 Loading review data...")
    
    if os.path.exists("data/reviews_with_themes.csv"):
        df = pd.read_csv("data/reviews_with_themes.csv")
        print(f"   Loaded {len(df)} reviews from reviews_with_themes.csv")
    elif os.path.exists("data/reviews_with_sentiment.csv"):
        df = pd.read_csv("data/reviews_with_sentiment.csv")
        print(f"   Loaded {len(df)} reviews from reviews_with_sentiment.csv")
    else:
        df = pd.read_csv("data/cleaned_reviews.csv")
        df["sentiment_label"] = "neutral"
        df["sentiment_score"] = 0.0
        df["identified_theme"] = "Other"
        print(f"   Loaded {len(df)} reviews from cleaned_reviews.csv")
    
    # Get bank_id mapping
    cursor.execute("SELECT bank_name, bank_id FROM banks")
    bank_map = {row[0]: row[1] for row in cursor.fetchall()}
    
    # Insert reviews
    print("\n💾 Inserting reviews into database...")
    inserted = 0
    
    for _, row in df.iterrows():
        try:
            cursor.execute("""
            INSERT INTO reviews (
                review_id, bank_id, review_text, rating, review_date,
                sentiment_label, sentiment_score, identified_theme, source
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (review_id) DO NOTHING
            """, (
                str(row.get("review_id", f"rev_{_}")),
                bank_map.get(row.get("bank", "Commercial Bank of Ethiopia"), 1),
                str(row.get("review_text", ""))[:1000],
                int(row.get("rating", 3)),
                str(row.get("review_date", "2024-01-01")),
                str(row.get("sentiment_label", "neutral")),
                float(row.get("sentiment_score", 0.0)),
                str(row.get("identified_theme", "Other")),
                "Google Play"
            ))
            inserted += 1
        except Exception as e:
            print(f"   Error on row {_}: {e}")
    
    conn.commit()
    print(f"✅ Inserted {inserted} reviews")
    
    # Verification queries
    print("\n" + "="*50)
    print("VERIFICATION RESULTS")
    print("="*50)
    
    cursor.execute("""
    SELECT b.bank_name, COUNT(r.review_id) 
    FROM banks b 
    LEFT JOIN reviews r ON b.bank_id = r.bank_id 
    GROUP BY b.bank_name
    """)
    print("\n📊 Reviews per bank:")
    for row in cursor.fetchall():
        print(f"   {row[0]}: {row[1]}")
    
    cursor.execute("SELECT COUNT(*) FROM reviews")
    total = cursor.fetchone()[0]
    print(f"\n✅ Total reviews in database: {total}")
    
    cursor.close()
    conn.close()
    
    print("\n" + "="*50)
    print("✅ DATABASE SETUP COMPLETE!")
    print("="*50)
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nMake sure:")
    print("1. PostgreSQL is running")
    print("2. Password is correct")
    print("3. Database 'bank_reviews' exists")

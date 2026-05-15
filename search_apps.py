from google_play_scraper import search

banks = ["Bank of Abyssinia", "Dashen Bank"]

for bank in banks:
    print("\n" + "="*40)
    print(f"Searching: {bank}")
    print("="*40)
    
    results = search(bank, n_hits=3)
    
    for app in results:
        print(f"App Name: {app.get('title')}")
        print(f"App ID: {app.get('appId')}")
        print(f"Rating: {app.get('score')} stars")
        print("-"*30)

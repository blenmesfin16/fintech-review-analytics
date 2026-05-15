from google_play_scraper import search

print("Searching for Bank of Abyssinia apps...")
print("="*50)

results = search("Bank of Abyssinia", n_hits=10)

for i, app in enumerate(results, 1):
    print(f"{i}. {app.get('title')}")
    print(f"   App ID: {app.get('appId')}")
    print(f"   Rating: {app.get('score')} stars")
    print(f"   Reviews: {app.get('ratings')}")
    print()

print("\n" + "="*50)
print("Searching for Dashen Bank apps...")
print("="*50)

results = search("Dashen Bank", n_hits=10)

for i, app in enumerate(results, 1):
    print(f"{i}. {app.get('title')}")
    print(f"   App ID: {app.get('appId')}")
    print(f"   Rating: {app.get('score')} stars")
    print(f"   Reviews: {app.get('ratings')}")
    print()

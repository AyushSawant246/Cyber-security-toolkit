import requests

# 1. Get user inputs
base_url = input("Enter base URL (e.g., http://example.com): ").rstrip('/')
wordlist_path = input("Enter path to wordlist file: ")

# 2. Load the wordlist
try:
    with open(wordlist_path, 'r') as f:
        entries = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("❌ Wordlist file not found.")
    exit(1)

print(f"\n🔍 Starting scan of {base_url} with {len(entries)} entries...\n")

# 3. Brute-force each entry
for entry in entries:
    url = f"{base_url}/{entry}"
    try:
        resp = requests.get(url, timeout=3)
        if resp.status_code in (200, 301, 302):
            print(f"[FOUND] {url} (Status: {resp.status_code})")
    except requests.RequestException:
        pass

print("\n✅ Scan complete.")

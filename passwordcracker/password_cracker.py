import time

# Ask the user to enter the password to be cracked
target_password = input("🔒 Enter the password to be cracked: ")

# Try to load the wordlist
try:
    with open("wordlist.txt", "r") as file:
        passwords = file.read().splitlines()
except FileNotFoundError:
    print("❌ wordlist.txt not found! Please make sure it's in the same directory.")
    exit()

# Start brute-force attack
print("\n🚀 Starting brute-force attack...\n")
start_time = time.time()

for attempt in passwords:
    print(f"🔍 Trying: {attempt}")
    if attempt == target_password:
        end_time = time.time()
        print("\n✅ Password cracked!")
        print(f"🔓 Password: {attempt}")
        print(f"⏱️ Time taken: {round(end_time - start_time, 2)} seconds")
        break
else:
    print("\n❌ Password not found in wordlist.")


import os
from cryptography.fernet import Fernet

# Generate a key (Run this once and save the key)
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as secret.key")

# Load the saved key
def load_key():
    if not os.path.exists("secret.key"):
        print("[❌] Key file not found! Please generate it using 'generate_key()' first.")
        exit(1)
    with open("secret.key", "rb") as key_file:
        return key_file.read()


# Encrypt a message
def encrypt_message(message, key):
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted

# Decrypt a message
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_message)
    return decrypted.decode()

# Main logic
def main():
    print("=== Encryption/Decryption Tool ===")
    choice = input("Do you want to (G)enerate key, (E)ncrypt, or (D)ecrypt? ").lower()

    if choice == 'g':
        generate_key()

    elif choice == 'e':
        key = load_key()
        message = input("Enter the message to encrypt: ")
        encrypted = encrypt_message(message, key)
        print(f"Encrypted message: {encrypted.decode()}")

    elif choice == 'd':
        key = load_key()
        encrypted_msg = input("Enter the encrypted message: ").encode()
        try:
            decrypted = decrypt_message(encrypted_msg, key)
            print(f"Decrypted message: {decrypted}")
        except:
            print("Invalid key or message!")

    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()

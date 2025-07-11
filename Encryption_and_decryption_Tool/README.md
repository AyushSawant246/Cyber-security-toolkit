# 🔐 Encryption/Decryption Tool

A simple Python-based tool for securely encrypting and decrypting text messages using Fernet symmetric encryption.

Perfect for beginners to understand how modern symmetric cryptography works.

--- 

## ✅ How it works

Generates a secret key file (secret.key) using Fernet symmetric encryption.

Encrypts a text message by taking your input and using the saved key.

Decrypts an encrypted message back to the original text using the same key.

Uses the cryptography library to handle secure encryption and decryption.

Prints the output in your terminal.

---

# ⚙️ Requirements

Python 3.x

cryptography library
   Install with:
   ```bash
   pip install cryptography
   ```
### 🚀 How to run

1. **Open terminal or command prompt**

2. **Navigate to the script’s folder:**
   ```bash
   cd path/to/Cyber-security-toolkit/Encryption_and_decryption_Tool

3. **Run the script:**
   ```bash
   python encdectool.py
   ```
4. **Follow the prompts:**

Generate a key (Run once to create secret.key file)

Encrypt any text using the saved key

Decrypt an encrypted message using the same key

### 💡 Example output

1. **🔑 Generate a key:**
   ```bash
   === Encryption/Decryption Tool ===
   Do you want to (G)enerate key, (E)ncrypt, or (D)ecrypt? G
   Key generated and saved as secret.key

2. **🔒 Encrypt a message:**
   ```bash
   === Encryption/Decryption Tool ===
   Do you want to (G)enerate key, (E)ncrypt, or (D)ecrypt? E
   Enter the message to encrypt: hello world
   Encrypted message: gAAAAABl...

3. **🔓 Decrypt a message:**
   ```bash
   === Encryption/Decryption Tool ===
   Do you want to (G)enerate key, (E)ncrypt, or (D)ecrypt? D
   Enter the encrypted message: gAAAAABl...
   Decrypted message: hello world

### 📝 Notes

Always generate your key before encrypting or decrypting.

Store secret.key safely — without it, your encrypted data cannot be
recovered!

Uses Fernet (AES in CBC mode with HMAC) for strong symmetric encryption.

### 🌱 Future Improvements

Add file encryption/decryption support.

Add automatic random message padding.

Cross-platform GUI version.

### 📂 Files

encdectool.py — main script

secret.key — generated encryption key (keep this secret!)

### ⚖️ License

MIT License — for educational and ethical use only.

## 🔒 Stay secure, encrypt everything! 🚀

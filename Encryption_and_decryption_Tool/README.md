🔐 Encryption/Decryption Tool

A simple Python-based tool for securely encrypting and decrypting text messages using Fernet symmetric encryption.

Perfect for beginners to understand how modern symmetric cryptography works.

⚙️ Requirements

Python 3.x

cryptography library

Install with:

bash

copy this ---> pip install cryptography

🚀 How to run

1️⃣ Open your terminal or command prompt.
2️⃣ Navigate to your script folder:

bash

copy this ---> cd path/to/Cyber-security-toolkit/Encryption_and_decryption_Tool

3️⃣ Run the script:

bash

copy this ---> python encdectool.py

4️⃣ Follow the prompts:

Generate a key (Run once to create secret.key file)

Encrypt any text using the saved key

Decrypt an encrypted message using the same key

💡 Example output

🔑 Generate a key:

=== Encryption/Decryption Tool ===
Do you want to (G)enerate key, (E)ncrypt, or (D)ecrypt? G
Key generated and saved as secret.key

🔒 Encrypt a message:

=== Encryption/Decryption Tool ===
Do you want to (G)enerate key, (E)ncrypt, or (D)ecrypt? E
Enter the message to encrypt: hello world
Encrypted message: gAAAAABl...

🔓 Decrypt a message:

=== Encryption/Decryption Tool ===
Do you want to (G)enerate key, (E)ncrypt, or (D)ecrypt? D
Enter the encrypted message: gAAAAABl...
Decrypted message: hello world

📝 Notes

✅ Always generate your key before encrypting or decrypting.
✅ Store secret.key safely — without it, your encrypted data cannot be recovered!
✅ Uses Fernet (AES in CBC mode with HMAC) for strong symmetric encryption.

🌱 Future Improvements

Add file encryption/decryption support.

Add automatic random message padding.

Cross-platform GUI version.

📂 Files

encdectool.py — main script

secret.key — generated encryption key (keep this secret!)

⚖️ License

MIT License — for educational and ethical use only.

🔒 Stay secure, encrypt everything! 🚀

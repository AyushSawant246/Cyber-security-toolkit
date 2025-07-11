# 🌐 Subdomain Scanner

A simple Python-based subdomain brute-forcer to discover active subdomains for a target domain using a basic wordlist.

---

## ✅ How it works

Takes a target domain (e.g., example.com).

Loops through a small list of common subdomain names (e.g., www, mail, ftp, admin).

Builds each subdomain URL like https://sub.example.com and checks if it’s active by sending an HTTP GET request.

Prints subdomains that return a 200 OK response.

---

### ⚙️ Requirements

Python 3.x

requests library

#### 🚀 How to run:

1. **Open terminal or command prompt**

2. **Install requests if you don’t have it:**
   ```bash
   pip install requests

3. **Navigate to the script’s folder:**
   ```bash
   cd path/to/Cyber-security-toolkit/reconnaissance

4. **Run the script:**
   ```bash
   python subdomain_scanner.py

5. **When prompted, enter your target domain:**

   ```bash
   Enter the target domain (e.g., google.com): google.com

6. **If it finds an active subdomain, you’ll see output like:**
   ```bash
   [ACTIVE] https://www.google.com
   [ACTIVE] https://mail.google.com

##### 💡 Basic wordlist

This version uses a hardcoded list of common subdomains:

["www", "mail", "ftp", "test", "admin", "blog", "dev", "shop"]

###### 📝 Notes

This is a basic proof-of-concept — it only checks if subdomains respond with HTTP 200.

It may not find all subdomains — for full scans, tools like Sublist3r or amass are better.

Use this script only on domains you own or have permission to test!

###### 🌱 Future Improvements

Use DNS resolution instead of just HTTP checks.

Add multi-threading for faster scanning.

Load subdomain wordlists from files.

Combine with passive sources like search engines.

###### 📂 Files

subdomain_scanner.py — main script

###### ⚖️ License

MIT License — for learning & educational purposes only.

**🔍 Happy Recon! 🚀**
# 🔍 Port Scanner

A simple Python-based TCP port scanner to find open ports on a target host within a specified port range.

--- 

## ✅ How it works

Uses Python’s socket module to attempt connections on each port in the given range.

Shows which ports are OPEN and their common service names (if found).

Has basic error handling and a timeout for slow or unreachable hosts.

---

### ⚙️ Requirements

Python 3.x

No external modules needed — uses built-in socket and argparse.

### 🚀 How to run

1. **Open terminal or command prompt**

2. **Navigate to the script’s folder:**
   ```bash
   cd path/to/Cyber-security-toolkit/network_tools

3. **Run the script: with following arguements**
   ```bash
   python port_scanner.py -t <target> -p <startPort-endPort>

Arguments:

-t or --target: IP address or domain name to scan

-p or --ports: Port range in the format start-end (e.g. 20-80)

--- 

### 💡 Example

1. ✅ Scan a port range:
   ```bash 
   python port_scanner.py -t google.com -p 20-80

2. ✅ Scan common ports 1-1024:
   ```bash
   python port_scanner.py -t 192.168.1.1 -p 1-1024

3. ✅ Scan a single port:
   ```bash
   python port_scanner.py -t example.com -p 80-80


### 📝 Notes

Uses a timeout of 1 second per port — adjust in the code if needed.

Tested on Windows Terminal & Kali Linux VM.

For educational use only — scan only systems you own or have permission to test.

### 📂 Files

port_scanner.py — main script.

### ⚖️ License

MIT License — use, share, and learn freely! 🔒✨

## ✅ Happy Scanning! ⚡
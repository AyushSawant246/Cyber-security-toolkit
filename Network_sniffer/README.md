🕵️‍♂️ Network Sniffer

A simple Python-based network sniffer that captures and displays network packets in real time.
Perfect for understanding how packets flow through your system.

✅ How it works

Uses raw sockets to capture all incoming/outgoing packets on your network interface.

Prints details like source IP, destination IP, protocol, and raw packet data.

Runs in promiscuous mode (if supported) to sniff packets not addressed directly to your machine.

⚙️ Requirements
Python 3.x

Requires admin/root privileges:

✅ On Windows: run as Administrator

✅ On Linux: run with sudo

🚀 How to run
Step 1: Open terminal or command prompt

Step 2: Navigate to the script location:

bash

copy this ----> cd path/to/Cyber-security-toolkit/network_tools

Step 3: Run the script:

bash 

copy this ----> python network_sniffer.py

💡 Example output

[+] 192.168.29.215 ---> 40.126.18.32 | Protocol: 6
[+] 40.126.18.32 ---> 192.168.29.215 | Protocol: 6
[+] 192.168.29.215 ---> 20.189.173.18 | Protocol: 6
[+] 20.189.173.18 ---> 192.168.29.215 | Protocol: 6
[+] 192.168.29.215 ---> 35.82.218.25 | Protocol: 6

Source IP --> Destination IP

Protocol: 6 means TCP (by IP protocol number).

📝 Notes
This is a basic sniffer — no advanced filtering, parsing, or saving packets yet.

Tested on Windows and Kali Linux (VMware).

Use responsibly — sniff only your own network or with permission!

🌱 Future Improvements
Add protocol parsing (TCP/UDP/ICMP headers).

Filter packets by port or protocol.

Save captured packets to a .pcap file for Wireshark analysis.

📂 Files
network_sniffer.py — main script

⚖️ License
MIT License — for educational use only.

🔍 Happy Sniffing! 📡✨
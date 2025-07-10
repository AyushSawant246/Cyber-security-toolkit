🔑 MAC Changer

A simple Python-based MAC address changer to spoof your network interface’s MAC address.
Useful for privacy, bypassing MAC filters, and learning basic ethical hacking operations.
✅ Works on Linux only

⚙️ Requirements
Python 3.x

Must run as root or with sudo privileges (required to change MAC).

🚀 How to run

1️⃣ Open your terminal.
2️⃣ Navigate to your script’s folder:

bash

copy this ---> cd path/to/Cyber-security-toolkit/network_tools

3️⃣ Run the script with root privileges:

bash
copy this ---> sudo python3 mac_changer.py

💡 Example output

Enter the interface name (e.g., eth0, wlan0): eth0
Current MAC: 08:00:27:12:34:56
Enter new MAC address (format: XX:XX:XX:XX:XX:XX): 00:11:22:33:44:55
MAC address was successfully changed to: 00:11:22:33:44:55

📝 Notes
✅ This script uses ifconfig or ip commands — tested on Linux only.

❌ On Windows, MAC addresses must be changed via Device Manager or a trusted tool like Technitium MAC Address Changer.

🔒 Always spoof your MAC responsibly — only on networks you own or have permission to test.

🌱 Future Improvements
Cross-platform support for Windows using registry editing.

Automatic random MAC generator option.

Multi-interface support.

📂 Files
mac_changer.py — main script

⚖️ License
MIT License — for educational and ethical hacking learning purposes only.

🕵️‍♂️ Stay hidden, stay ethical! 🚀
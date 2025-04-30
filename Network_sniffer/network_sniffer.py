from scapy.all import sniff, IP

# Callback function to process captured packets
def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto
        print(f"[+] {ip_src} --> {ip_dst} | Protocol: {proto}")

# Start sniffing
print("🚨 Sniffing... Press Ctrl+C to stop.")
sniff(filter="ip", prn=packet_callback, store=0)

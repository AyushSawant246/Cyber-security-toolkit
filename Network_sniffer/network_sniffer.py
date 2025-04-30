from scapy.all import sniff, IP
packet_limit = int(input("Enter number of packets to capture (default 10): ") or 10)
packets = sniff(count=packet_limit)
user_filter = input("Enter filter (e.g., 'tcp port 80') or press Enter for no filter: ")
packets = sniff(count=packet_limit, filter=user_filter)
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

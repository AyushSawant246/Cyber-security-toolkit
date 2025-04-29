import socket
import argparse

parser = argparse.ArgumentParser(description="Basic Port Scanner")

parser.add_argument("-t", "--target", help="Target IP address", required=True)
parser.add_argument("-p", "--ports", help="Port range (e.g. 20-80)", default="1-1024")

args = parser.parse_args()
target = args.target
start_port, end_port = map(int, args.ports.split('-'))

print(f"\n[+] Scanning target: {target}\n")

for port in range(start_port, end_port + 1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout for slow ports
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
            print(f"[OPEN] Port {port} ({socket.getservbyport(port)})")
        sock.close()
    except KeyboardInterrupt:
        print("\nExiting...")
        break
    except socket.gaierror:
        print("Hostname could not be resolved.")
        break
    except socket.error:
        print("Could not connect to server.")
        break

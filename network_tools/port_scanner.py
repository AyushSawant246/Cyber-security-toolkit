import socket

# Target (you can hardcode or use input())
target = input("Enter target IP or domain: ")

# Common ports to scan
ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

print(f"\n[+] Scanning target: {target}\n")

for port in ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout for slow ports
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
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

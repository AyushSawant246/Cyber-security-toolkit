import subprocess
import re

def get_current_mac(interface):
    try:
        output = subprocess.check_output(["ifconfig", interface]).decode()
        mac_address = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", output)
        if mac_address:
            return mac_address.group(0)
        else:
            return None
    except:
        return None

def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])

def main():
    interface = input("Enter the interface name (e.g., eth0, wlan0): ")
    current_mac = get_current_mac(interface)
    
    if current_mac:
        print(f"Current MAC: {current_mac}")
    else:
        print("Could not read current MAC address.")
        return

    new_mac = input("Enter new MAC address (format: XX:XX:XX:XX:XX:XX): ")
    change_mac(interface, new_mac)
    
    updated_mac = get_current_mac(interface)
    if updated_mac == new_mac:
        print(f"[✔] MAC address changed successfully to {updated_mac}")
    else:
        print("[❌] MAC address change failed.")

if __name__ == "__main__":
    main()

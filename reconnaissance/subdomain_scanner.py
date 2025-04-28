print("Subdomain Scanner Tool Loaded!")
import requests # type: ignore

def find_subdomains(domain, subdomains):
    print(f"\n[+] Finding subdomains for: {domain}\n")
    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"[ACTIVE] {url}")
        except requests.ConnectionError:
            pass

if __name__ == "__main__":
    domain = input("Enter the target domain (e.g., google.com): ")
    
    # Basic subdomains list
    subdomains = ["www", "mail", "ftp", "test", "admin", "blog", "dev", "shop"]
    
    find_subdomains(domain, subdomains)


import requests

def find_subdomains(domain, subdomains):
    print(f"\n[+] Finding subdomains for: {domain}\n")
    for subdomain in subdomains:
        url = f"https://{subdomain}.{domain}"
        try:
            response = requests.get(url)
            if response.status_code < 400:
                print(f"[ACTIVE] {url}")
        except requests.ConnectionError:
            pass
        except requests.exceptions.RequestException:
            pass

if __name__ == "__main__":
    domain = input("Enter the target domain (e.g., google.com): ")
    
    with open("subdomains.txt") as file:
     subdomains = file.read().splitlines()

    
    find_subdomains(domain, subdomains)


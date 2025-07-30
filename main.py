import requests
from bs4 import BeautifulSoup

def fetch_whois(domain):
    """Fetch WHOIS information for a given domain."""
    url = f"https://whois.domaintools.com/{domain}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find('pre').text if soup.find('pre') else "WHOIS info not found"

def fetch_ip_info(ip):
    """Fetch IP geolocation information."""
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    return response.json()

def search_google(query):
    """Search Google and return the titles and links."""
    url = f"https://www.google.com/search?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for g in soup.find_all('h3'):
        link = g.find_parent('a')['href']
        results.append((g.text, link))
    return results

def main():
    domain = input("Enter the domain: ")
    print("\nFetching WHOIS information...")
    print(fetch_whois(domain))

    ip = input("\nEnter the IP address: ")
    print("\nFetching IP information...")
    ip_info = fetch_ip_info(ip)
    print(ip_info)

    query = input("\nEnter a search query: ")
    print("\nSearching Google...")
    results = search_google(query)
    for title, link in results:
        print(f"{title}: {link}")

if __name__ == "__main__":
    main()
import requests
from bs4 import BeautifulSoup

# Basic Website Scraper
def website_scraper(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Extracting titles from an HTML page
    titles = soup.find_all('h2')
    for title in titles:
        print(title.text)

# Run the Website Scraper
website_scraper('https://example.com')

import requests
from bs4 import BeautifulSoup

# Specify the URL of the website to be scraped
url = "https://www.google.com"

try:
    # Send an HTTP GET request to the specified URL
    response = requests.get(url)

    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all anchor elements in the HTML
    links = soup.find_all('a')

    # Print the "href" attributes of the anchor elements
    for link in links:
        print(link.get('href'))

except requests.exceptions.RequestException as e:
    # Handle request exceptions (e.g., connection issues)
    print(f"Error: {e}")
except Exception as e:
    # Handle other exceptions (e.g., parsing errors)
    print(f"Error: {e}")

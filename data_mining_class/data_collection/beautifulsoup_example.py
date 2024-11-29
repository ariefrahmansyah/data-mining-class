import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/Data_mining"

# Send a request to the webpage
response = requests.get(url)

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find and extract all headings
headings = soup.find_all("h2")
print("Headings:")
for heading in headings:
    print(heading.text)

# Find and extract all links
links = soup.find_all("a")
print("\nLinks:")
for link in links:
    print(link.get("href"), link.text)

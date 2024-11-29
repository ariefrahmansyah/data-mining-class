import requests
from bs4 import BeautifulSoup

url = "https://mi.amikom.ac.id/page/dosen"

# Send a request to the webpage
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

lecturers = soup.find_all("div", class_="font-bold text-xl mb-2")
print("Lecturers:")
for lecturer in lecturers:
    print(lecturer.text)

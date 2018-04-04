import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Room_641A"


r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
for item in soup.select('.mw-headline'):
    print(item.text)





import requests 
res = requests.get("https://randomuser.me/")
import bs4
soup = bs4.BeautifulSoup(res.text,('lxml'))

(soup.select('h1'))
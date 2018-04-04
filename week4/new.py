import requests
from bs4 import BeautifulSoup
url = "https://randomuser.me"

def get_some_details():
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    
    #lastname
    #for item in soup.select('#user_value'):
    #    print(item.text) 
    for item in soup.select('.active'):
        print(item.text)
  

get_some_details()
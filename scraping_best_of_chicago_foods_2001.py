from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://www.chicagoreader.com"

def make_soup(url):
    response = urlopen(url).read()
    return BeautifulSoup(response, "html.parser")

def get_section_urls():
    soup = make_soup(BASE_URL)
    links = soup.find_all('a')
    for link in links:
        if 'http' in link.get('href'):
            if '/Section' in link.get('href'):
                print link.get('href'), " :: ", link.text
   
print get_section_urls()


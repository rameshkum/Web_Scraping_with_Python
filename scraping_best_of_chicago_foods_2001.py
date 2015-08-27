from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://www.chicagoreader.com"

def make_soup(url):
    response = urlopen(url).read()
    return BeautifulSoup(response, "html.parser")

print make_soup(BASE_URL)


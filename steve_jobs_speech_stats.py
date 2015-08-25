# Lists YouTube statistics of Steve Jobs 2005 Speech
# Todo's: find likes and dislikes count

import requests
import re
from bs4 import BeautifulSoup

root_url = 'https://www.youtube.com/watch?v=UF8uR6Z6KLc'

def get_video_stats(root_url):
    video_data = {}
    response = requests.get(root_url)
    soup = BeautifulSoup(response.text, "html.parser")
    video_data['title'] = soup.select('div#watch-headline-title span')[0].get_text()
    video_data['views'] = int(re.sub('[^0-9]', '', soup.select('.watch-view-count')[0].get_text().split()[0]))
    return video_data

print get_video_stats(root_url)
    





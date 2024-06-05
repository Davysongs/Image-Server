import requests
from bs4 import BeautifulSoup
import os

def scrape_menu_images(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = []
    for img in soup.find_all('img'):
        img_url = img['src']
        img_response = requests.get(img_url)
        img_name = os.path.join('src/data', img_url.split('/')[-1])
        with open(img_name, 'wb') as f:
            f.write(img_response.content)
        images.append(img_name)
    return images

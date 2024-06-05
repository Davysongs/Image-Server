import requests
from bs4 import BeautifulSoup
import os
import re

def sanitize_filename(filename):
    """
    Remove or replace invalid characters in filenames.
    """
    return re.sub(r'[\\/*?:"<>|]', "_", filename)

def scrape_menu_images(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)

    soup = BeautifulSoup(response.text, 'html.parser')
    images = []
    for img in soup.find_all('img'):
        img_url = img.get('src')
        if img_url and img_url.startswith('http'):
            img_response = requests.get(img_url, headers=headers)
            img_response.raise_for_status()
            # Sanitize the image filename
            img_name = os.path.join('src/data', sanitize_filename(os.path.basename(img_url)))
            with open(img_name, 'wb') as f:
                f.write(img_response.content)
            images.append(img_name)
    return images

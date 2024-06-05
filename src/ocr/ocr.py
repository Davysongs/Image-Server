import pytesseract
from PIL import Image
import re
import os
from dotenv import load_dotenv

load_dotenv()

# Set the Tesseract command path from environment variable
pytesseract.pytesseract.tesseract_cmd = os.getenv("TESSERACT_CMD")

def extract_menu_items(text):
    menu_items = []
    lines = text.split('\n')
    for line in lines:
        match = re.match(r'(.+?)\s+\$?(\d+\.\d{2})', line)
        if match:
            item = match.group(1).strip()
            price = float(match.group(2).strip())
            menu_items.append({'name': item, 'price': price})
    return menu_items

def perform_ocr(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return extract_menu_items(text)

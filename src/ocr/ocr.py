import pytesseract
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()

# Set the Tesseract command path from environment variable
pytesseract.pytesseract.tesseract_cmd = os.getenv("TESSERACT_CMD")

def perform_ocr(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    # Here you should process the text to extract menu items and prices
    return text

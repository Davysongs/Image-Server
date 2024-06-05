from src.scraper.scraper import scrape_menu_images
from src.ocr.ocr import perform_ocr
from src.database.database import store_menu_data
import os

def main():
    # Step 1: Scrape menu images
    images = scrape_menu_images("https://www.example.com/mumbai-restaurants")

    # Step 2: Perform OCR on the images
    menu_data = []
    for image in images:
        data = perform_ocr(image)
        menu_data.append(data)

    # Step 3: Store the extracted data in the database
    store_menu_data(menu_data)

if __name__ == "__main__":
    main()

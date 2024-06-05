import csv
from src.scraper.scraper import scrape_menu_images
from src.ocr.ocr import perform_ocr
from src.database.database import store_menu_data
import os

def read_restaurant_links(csv_file):
    links = []
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            links.append(row['restaurant_url'])
    return links

def main():
    # Read restaurant links from CSV
    csv_file = 'data/restaurants.csv'
    restaurant_links = read_restaurant_links(csv_file)

    all_menu_data = []

    for link in restaurant_links:
        print(f"Processing {link}")
        
        #Scrape menu images
        images = scrape_menu_images(link)
        
        #Perform OCR on the images
        menu_data = []
        for image in images:
            data = perform_ocr(image)
            menu_data.extend(data)
        
        all_menu_data.extend(menu_data)

    # Store the extracted data in the database
    store_menu_data(all_menu_data)

if __name__ == "__main__":
    main()

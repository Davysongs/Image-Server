import csv
import time
import os
from requests.exceptions import ConnectionError, Timeout, RequestException
from src.scraper.scraper import scrape_menu_images
from src.ocr.ocr import perform_ocr
from src.database.database import store_menu_data, create_database
from dotenv import load_dotenv

load_dotenv()

def read_restaurant_links(csv_file):
    links = []
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            links.append(row['restaurant_url'])
    return links

def main():
    # Read restaurant links from CSV
    csv_file = 'restaurants.csv'
    restaurant_links = read_restaurant_links(csv_file)

    all_menu_data = []

    for link in restaurant_links:
        print(f"Processing {link}")

        # Initialize images list
        images = []

        # Retry logic with exponential backoff
        retries = 5
        for attempt in range(retries):
            try:
                # Step 1: Scrape menu images
                images = scrape_menu_images(link)
                print(f"Successfully scraped {len(images)} images from {link}")
                break  # Exit the retry loop if successful
            except (ConnectionError, Timeout) as e:
                wait = 2 ** attempt  # Exponential backoff
                print(f"Error: {e}. Retrying in {wait} seconds...")
                time.sleep(wait)
            except RequestException as e:
                print(f"RequestException: {e}. Skipping this link.")
                break
        else:
            print(f"Failed to scrape {link} after {retries} attempts")
            continue  # Skip to the next link if all retries fail

        # Step 2: Perform OCR on the images
        menu_data = []
        print(f"performing ocr on images...")
        for image in images:
            data = perform_ocr(image)
            menu_data.extend(data)

        all_menu_data.extend(menu_data)

    # Step 3: Store the extracted data in the database
    try:
        print('storing data received to database')
        print(all_menu_data)
        store_menu_data(all_menu_data)
    except Exception as e:
        print(f"Error storing data: {e}")

if __name__ == "__main__":
    # Check if the database exists, if not, create it
    create_database()
    main()

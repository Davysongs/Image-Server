import unittest
from src.scraper.scraper import scrape_menu_images

class TestScraper(unittest.TestCase):
    def test_scrape_menu_images(self):
        images = scrape_menu_images("https://www.example.com/mumbai-restaurants")
        self.assertTrue(len(images) > 0)

if __name__ == '__main__':
    unittest.main()

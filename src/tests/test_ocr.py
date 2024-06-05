import unittest
from src.ocr.ocr import perform_ocr

class TestOCR(unittest.TestCase):
    def test_perform_ocr(self):
        text = perform_ocr("src/data/sample_menu.jpg")
        self.assertTrue(len(text) > 0)

if __name__ == '__main__':
    unittest.main()

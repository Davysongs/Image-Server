#Restaurant Menu Scraper

This project scrapes restaurant menu images for restaurants in Mumbai, performs OCR (Optical Character Recognition) to read the menu items and prices, and stores this data in a database.

## Table of Contents

- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Testing](#testing)
- [Environment Variables](#environment-variables)

## Project Structure

```markdown
project_root/
│
├── README.md
├── requirements.txt
├── .env
├── restaurants.csv
├── main.py
├── src/
│   ├── __init__.py
│   ├── scraper/
│   │   ├── __init__.py
│   │   ├── scraper.py
│   ├── ocr/
│   │   ├── __init__.py
│   │   ├── ocr.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── database.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_scraper.py
│   │   ├── test_ocr.py
│   │   ├── test_database.py
│   ├── data/
│       ├── (This directory will store any temporary files, such as downloaded images)
```

## Technologies Used

- **Python 3.7+**
- **Libraries**:
  - `requests` for web scraping
  - `BeautifulSoup` for parsing HTML
  - `Pillow` for image handling
  - `pytesseract` for OCR
  - `SQLAlchemy` for database interactions
  - `python-dotenv` for environment variable management
  - `pytest` for testing

## Setup Instructions

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Davysongs/Image-Server.git
   cd Image-Server
   ```

2. **Create a virtual environment and activate it**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required libraries**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Install Tesseract OCR**:
   - **Windows**: Download and install from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
   - **macOS**: Install using Homebrew:
     ```sh
     brew install tesseract
     ```
   - **Linux**: Install using the package manager:
     ```sh
     sudo apt-get install tesseract-ocr
     ```

5. **Set up the environment variables**:
   - Create a `.env` file in the project root and add the following variables:
     ```env
     DATABASE_URL=sqlite:///menus.db
     TESSERACT_CMD=/path/to/tesseract  # Replace with the actual path to the Tesseract executable
     ```

## How It Works

1. **Scraping Menu Images**:
   - The script reads restaurant URLs from a CSV file (`restaurants.csv`).
   - For each URL, it scrapes menu images using `requests` and `BeautifulSoup`.
   - Images are saved in the `src/data` directory after sanitizing the filenames.

2. **Performing OCR**:
   - The script performs OCR on the saved images using `pytesseract`.
   - Extracted text is processed to identify menu items and prices.

3. **Storing Data in Database**:
   - Extracted menu items and prices are stored in an SQLite database using `SQLAlchemy`.

## Usage

1. **Prepare the CSV file**:
   - Create or update `restaurants.csv` with the restaurant names and URLs in the following format:
     ```csv
     restaurant_name,restaurant_url
     Restaurant A,https://www.example.com/restaurant-a-menu
     Restaurant B,https://www.example.com/restaurant-b-menu
     ```

2. **Run the main script**:
   ```sh
   python main.py
   ```

## Testing

Run the tests using `pytest`:
```sh
pytest
```

## Environment Variables

- **`DATABASE_URL`**: URL for the SQLite database (default is `sqlite:///menus.db`).
- **`TESSERACT_CMD`**: Path to the Tesseract OCR executable.

## Additional Information

- **Ensure that Tesseract OCR is installed and the path is correctly set in the environment variables**.
- **The `data` directory is automatically created if it doesn't exist**.
- **The script includes retry logic with exponential backoff to handle connection issues gracefully**.

This project demonstrates a comprehensive approach to web scraping, OCR processing, and database management using Python. Follow the setup instructions carefully to ensure a smooth operation.

### Explanation

1. **Project Structure**: Provides an overview of the project's directory layout.
2. **Technologies Used**: Lists the technologies and libraries used in the project.
3. **Setup Instructions**: Guides users through cloning the repository, setting up a virtual environment, installing dependencies, and configuring environment variables.
4. **How It Works**: Explains the workflow of scraping, performing OCR, and storing data.
5. **Usage**: Instructions on preparing the CSV file and running the main script.
6. **Testing**: Instructions for running tests using `pytest`.
7. **Environment Variables**: Details the required environment variables and their purposes.
8. **Additional Information**: Includes important notes on Tesseract OCR installation and script behavior.

# Job Parser Automation with Selenium

This is a Python-based job parser that automates the process of scraping job listings from [robota.ua](https://robota.ua) using Selenium. The script navigates the website, applies filters, collects job titles and URLs, and saves the results in both Excel and text file formats.

---

## Features

- **Web Automation**: Uses Selenium to interact with the website dynamically.
- **Filters Support**: Automatically applies filters such as "No Experience" (`Без досвіду`).
- **Pagination Handling**: Navigates through multiple pages to extract all job listings.
- **Data Export**: Saves the extracted data in:
  - Excel (`.xlsx`) format using `openpyxl`.
  - Text (`.txt`) file format.

---

## Technologies Used

- **Python 3.9+**
- **Selenium**: For web scraping and browser automation.
- **WebDriver Manager**: Automatically manages ChromeDriver.
- **Pandas**: For structuring and exporting data.
- **OpenPyXL**: For exporting data to Excel.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/KarasunoAs9/parser.git
   cd parser
   ```
2. Create a virtual environment and activate it:
    ```bash
      python -m venv .venv
      source .venv/bin/activate #For windows
      source .venv/bin/activate #For Linux/MacOS
   ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the script:
   ```bash
   python parser.py
   ```

     

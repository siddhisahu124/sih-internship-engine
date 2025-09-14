import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import requests

# New imports for the wait condition
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def scrape_aicte_internships():
    """
    Scrapes internship data from the AICTE Internship Portal using Selenium
    to handle dynamically loaded content.
    """
    print("Setting up WebDriver...")
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    except Exception as e:
        print(f"Error setting up WebDriver. Make sure Chrome is installed and updated. {e}")
        return []

    url = "https://internship.aicte-india.org/index.php"
    print("Opening webpage with Selenium...")
    driver.get(url)

    # Smart Wait Condition
    # This tells Selenium to wait for up to 20 seconds until an element with the
    # class 'internship-list' is visible on the page.
    print("Waiting for internship listings to load...")
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "internship-list"))
        )
        print("Internships found! Getting page source.")
    except Exception as e:
        print(f"Timed out while waiting for listings. {e}")
        driver.quit()
        return []

    # Get the page source after dynamic content has loaded
    page_source = driver.page_source
    driver.quit()

    soup = BeautifulSoup(page_source, 'html.parser')

    # UPDATED: Use the new combined class name
    internship_cards = soup.find_all('div', class_='card internship-item')

    if not internship_cards:
        print("No internship listings found on the page. The website structure might have changed.")
        return []

    print(f"Found {len(internship_cards)} internships. Parsing details...")
    
    all_internships = []
    
    # ... (rest of your extraction logic here) ...
    # This logic from our previous conversation should still be correct.
    
    return all_internships

if __name__ == '__main__':
    print("Starting AICTE Internship Scraper...")
    internships = scrape_aicte_internships()
    
    if internships:
        print(f"\nSuccessfully scraped {len(internships)} internships.")
        df = pd.DataFrame(internships)
        output_filename = "aicte_internships.csv"
        df.to_csv(output_filename, index=False)
        print(f"Data saved to {output_filename}")
        print("\nFirst 5 internships:")
        print(df.head())
    else:
        print("Scraping finished with no data.")
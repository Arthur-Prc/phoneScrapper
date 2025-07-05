import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm
import time

# Load CSV
df = pd.read_csv('contacts.csv')

# Set up Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Remove this to see the browser
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

def extract_phone(url):
    try:
        driver.get(url)

        # Handle popup
        try:
            enter_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'enter')]")))
            enter_button.click()
            print("Popup closed")
        except:
            print("No popup found or already closed")

        # Click 'contact me' button
        try:
            contact_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'contact me')]")))
            contact_button.click()
            print("Clicked contact me")
        except:
            print("Contact button not found")
            return "Phone not found"

        # Wait for number to appear and extract it
        time.sleep(2)
        phone_elements = driver.find_elements(By.XPATH, "//*[contains(text(), '+') or contains(text(), '(')]")
        for el in phone_elements:
            text = el.text.strip()
            if any(char.isdigit() for char in text) and len(text) >= 8:
                return text

        return "Phone not found"

    except Exception as e:
        print(f"Error with {url}: {e}")
        return "Phone not found"

# Process each row with progress bar
for index, row in tqdm(df.iterrows(), total=len(df), desc="Processing"):
    if pd.isna(row['Phone']) or row['Phone'] == '':
        phone = extract_phone(row['Link'])
        df.at[index, 'Phone'] = phone
        print(f"{row['Name']}: {phone}")

# Save updated CSV
df.to_csv('contacts_updated.csv', index=False)
driver.quit()

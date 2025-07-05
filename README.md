# phoneScrapper
This script reads a CSV with columns: Link, Name, Phone. It opens each link, closes any popup, clicks 'contact me', and extracts the phone number.
Web Scraper with Selenium - README & Installation
Installation Steps (Windows):
1. Install Python from https://www.python.org (ensure to check "Add Python to PATH" during
installation).
2. Open Command Prompt (Win + R -> type: cmd -> Enter).
3. Run the following to install dependencies:
 pip install selenium pandas tqdm
4. Download ChromeDriver matching your Chrome version:
 - Find your version: chrome://settings/help
 - Download: https://chromedriver.chromium.org/downloads
 - Extract 'chromedriver.exe' and place it in the same folder as the script or add to your system
PATH.
Script Overview
This script reads a CSV with columns: Link, Name, Phone.
It opens each link, closes any popup, clicks 'contact me', and extracts the phone number.
Features:
- Handles popups with flexible matching (like "enter rentmen-eu", "accept", "ok", "close").
- Uses a progress bar (tqdm).
- Writes "Phone not found" if the number isn't found.
- Saves results in 'contacts_updated.csv'.
Sample contacts.csv Format
Link,Name,Phone
https://example.com/profile1,John,
https://example.com/profile2,Anna,
You're ready to run the script!

### 📱 **phoneScrapper – Web Scraper with Selenium**

A Python script that:

* Reads a CSV file with contact links
* Opens each link using Selenium
* Closes popups and clicks the “contact me” button
* Extracts the phone number (if available)
* Saves results to a new CSV

---

### 📦 **Installation Steps (Windows)**

1. **Install Python**

   * Download from: [python.org](https://www.python.org)
   * During install, check ✅ **"Add Python to PATH"**

2. **Install Dependencies**

   * Open **Command Prompt** (`Win + R` → type `cmd` → hit Enter)
   * Run:

     ```bash
     pip install selenium pandas tqdm
     ```

3. **Install ChromeDriver**

   * Find your Chrome version: `chrome://settings/help`
   * Download matching ChromeDriver: [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads)
   * Extract `chromedriver.exe`:

     * Option A: Place it in the **same folder** as the script
     * Option B: Add it to your **system PATH**

---

### 🔍 **Script Overview**

* **Input**: CSV file with columns:
  `Link, Name, Phone`

* **Functionality**:

  * Opens each URL from the CSV
  * Closes popups using flexible matching (e.g., buttons with text "enter rentmen-eu", "accept", "ok", "close")
  * Clicks the "contact me" button
  * Extracts the displayed phone number

* **Output**:

  * Writes phone numbers (or “Phone not found”) back to a new file:
    `contacts_updated.csv`

---

### 🌟 **Features**

* ✅ Handles multiple popup formats
* ⏳ Displays a real-time progress bar (via `tqdm`)
* ❌ Logs “Phone not found” if no number is found
* 💾 Saves results automatically to `contacts_updated.csv`

---

### 📄 **Sample `contacts.csv` Format**

```csv
Link,Name,Phone
https://example.com/profile1,John,
https://example.com/profile2,Anna,
```

---

### 🚀 **You're Ready to Run the Script!**

* Ensure `chromedriver.exe` is in place
* Make sure your `contacts.csv` file is prepared correctly
* Launch the script using Python in the terminal:

  ```bash
  python phoneScrapper.py
  ```

# Automated Hash Decrypter with Web Scraping

## Overview
This Python script automates the process of hash decryption using web scraping techniques. It utilizes the Selenium library to interact with a hash decryption website (in this case, 'https://www.cmd5.org/').

## Requirements
- Python 3.x
- Selenium library
- ChromeDriver (compatible version with your Chrome browser)

## Installation

1. Install Python 3.x: [Python Official Website](https://www.python.org/downloads/)

2. Install Selenium library:
    ```bash
    pip install selenium
    ```

3. Download ChromeDriver: [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)

4. Extract the ChromeDriver executable and provide its path in the script:
    ```python
    service = Service(executable_path='path/to/chromedriver')
    ```

## Usage

1. Open the script in a text editor or an integrated development environment (IDE).

2. Update the ChromeDriver executable path:
    ```python
    service = Service(executable_path='path/to/chromedriver')
    ```

3. Replace the hash value in the script with the one you want to decrypt:
    ```python
    input_field.send_keys('your_hash_value_here')
    ```

4. Run the script:
    ```bash
    python script_name.py
    ```

## Important Note
Ensure that your ChromeDriver version matches your Chrome browser version for compatibility.

## Description
The script uses Selenium to automate the following steps:
1. Navigate to 'https://www.cmd5.org/'.
2. Input the hash value into the designated field.
3. Trigger the change event on the input field using JavaScript.
4. Click the decryption button.
5. Wait for the decryption process to complete and print the result.

Feel free to customize the script based on the website's structure and requirements.

**Disclaimer:** Ensure compliance with the terms of service of the website being scraped. Web scraping without permission may violate terms of service and legal agreements. Use this script responsibly and only on websites where scraping is allowed.

## Credits
This script is for educational purposes only and is inspired by the need for hash decryption automation. Credits to the Selenium development team for the powerful automation capabilities provided by the library.

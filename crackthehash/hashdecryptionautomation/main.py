

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path='chromedriver')
options = webdriver.ChromeOptions()


driver = webdriver.Chrome(service=service, options=options)


# Initialize the WebDriver (this example uses Chrome)

# Navigate to the website
driver.get('https://www.cmd5.org/')

# Find the input field and click it
input_field = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_TextBoxInput')
input_field.send_keys('48bb6e862e54f2a795ffc4e541caed4d')


# Trigger the change event on the input field using JavaScript
driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", input_field)

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_Button1"))
)

# Use pyautogui to press 'enter' instead of button.click()
button.click()

# Wait for the output to be populated and print it
try:
    def text_is_not_wait(driver):
        element = driver.find_element(By.ID, 'LabelAnswer')  # Finding the referenced element
        if element.text != 'wait...':
            print("loading...")
            return element
        else:
            print("loading...")
            return False


    # Wait for the span to be populated with the desired text
    wait = WebDriverWait(driver, 2)
    span = wait.until(text_is_not_wait)

    # Print the span's text
    print(span.text)
finally:
    driver.quit()

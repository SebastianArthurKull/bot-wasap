import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome webdriver
driver = webdriver.Chrome()

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")
print("Please scan the QR code to log in...")

# Wait for the user to connect their phone to WhatsApp Web
wait = WebDriverWait(driver, 600)  # Adjust the timeout as needed

# Define attributes of the span element
span_attributes = {
    "dir": "auto",
    "title": input("add name of your friend: "),
}

# Wait for the span element to become present in the DOM
span_element = wait.until(EC.presence_of_element_located((By.XPATH, f'//span[@dir="{span_attributes["dir"]}"][@title="{span_attributes["title"]}"]')))
span_element.click()

text_to_spam = input("what message you want to spam: ")

while True:

    driver.switch_to.active_element.send_keys(text_to_spam)
    driver.switch_to.active_element.send_keys(Keys.RETURN)
    random_float = random.uniform(0.1, 1)
    time.sleep(0)

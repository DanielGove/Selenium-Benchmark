
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://humanbenchmark.com/tests/typing")

# Click on the text box
text_box = WebDriverWait(driver, timeout=5).until(
    lambda d: d.find_element(By.XPATH, "*//div[@class='letters notranslate']")
)
text_box.click()

# Type the appropriate letters
# First method: One character at a tim3:
"""
while True:
    try:
        character = driver.find_element(By.XPATH, "//span[@class='incomplete current']").text
        if not character:
            text_box.send_keys(' ')
        else:
            text_box.send_keys(character)
    except:
        break
"""
# Second method: All at once
# This method is far superior.
first_character = WebDriverWait(driver, timeout=5).until(
    lambda d: d.find_element(By.XPATH, "//span[@class='incomplete current']")
).text

other_characters = list(map(lambda E: E.text, driver.find_elements(By.XPATH, "//span[@class='incomplete']")))
for i in range(len(other_characters)):
    if not other_characters[i]:
        other_characters[i] = " "

full_text = ''.join([first_character] + other_characters)
text_box.send_keys(full_text)

input()

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://humanbenchmark.com/tests/verbal-memory")

# Press the start button
WebDriverWait(driver, timeout=5).until(
    lambda d: d.find_element(By.XPATH, "//button[text()='Start']")
).click()

word_set = set()
while True:
    word = WebDriverWait(driver, timeout=5).until(
        lambda d: d.find_element(By.CLASS_NAME, "word")
    ).text

    if word in word_set:
        # Click the "seen" button
        driver.find_element(By.XPATH, "//button[text()='SEEN']").click()
    else:
        word_set.add(word)
        # Click the "new" button
        driver.find_element(By.XPATH, "//button[text()='NEW']").click()

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://humanbenchmark.com/tests/memory")

# Press the start button
WebDriverWait(driver, timeout=5).until(
    lambda d: d.find_element(By.XPATH, "//*[text()='Start']")
).click()

while True:
    active_tiles = WebDriverWait(driver, timeout=5).until(
        lambda d: d.find_elements(By.XPATH, "//div[@class='active css-lxtdud eut2yre1']")
    )

    time.sleep(1.2)

    for tile in active_tiles:
        tile.click()

    time.sleep(1.2)
import time
start_time = time.time()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://humanbenchmark.com/tests/chimp")

# Press the start button
WebDriverWait(driver, timeout=5).until(
    lambda d: d.find_element(By.XPATH, "//*[text()='Start Test']")
).click()

# Start The Game
level = 4
while True:
    for i in range(level):
        tile = WebDriverWait(driver, timeout=10).until(
            lambda d: d.find_element(By.XPATH, f"//*[@data-cellnumber='{i+1}']")
        )
        tile.click()

    # Must press the continue button.
    try:
        WebDriverWait(driver, timeout=10).until(
            lambda d: d.find_element(By.XPATH, "//*[text()='Continue']")
        ).click()
    except:
        print(f"Executed in {time.time()-start_time} seconds.")
        break
    level += 1
input()
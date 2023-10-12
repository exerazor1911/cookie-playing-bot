from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

timeout = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie.click()

    if time.time() > timeout:

        upgrades = driver.find_elements(By.CSS_SELECTOR, value="#store div:not(.grayed)")

        selected_upgrade = upgrades[-1]

        selected_upgrade.click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookies_per_s = driver.find_element(By.ID, "cps").text
        print(cookies_per_s)
        break

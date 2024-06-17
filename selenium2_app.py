from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import os
from app import get_options

#リストのインポート
items = get_options()

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5000/")


for area in items:

    dropdown = driver.find_element(By.ID, 'options')

    select = Select(dropdown)

    select.select_by_value(area)

    print("通過1")

    search_button = driver.find_element(By.XPATH, "/html/body/form/button")

    search_button.click()

    print("通過2")

    # スクリーンショットを保存
    screenshot_path = os.path.join("screenshot", f'screenshot_{area}.png')
    driver.save_screenshot(screenshot_path)

    print("通過3")

driver.quit()


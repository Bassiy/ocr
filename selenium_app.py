from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app import get_options

#リストのインポート
items = get_options()


'''
サイトを開く
'''

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5000/")

print("通過1")

'''
プルダウンを選択
'''
# ドロップダウンリストを取得するために:select name="options" id="options"これね
dropdown = driver.find_element(By.ID, 'options')

# Select オブジェクトを生成。
select = Select(dropdown)

select.select_by_value("愛知県")

print("通過2")


'''
ボタンクリック：XPATHで取る
'''
search_button = driver.find_element(By.XPATH, "/html/body/form/button")

search_button.click()

print("通過3")

'''
スクリーンショット
'''
# スクリーンショットを保存
driver.save_screenshot('screenshot.png')

print("通過4")

'''
終了
'''

driver.quit()

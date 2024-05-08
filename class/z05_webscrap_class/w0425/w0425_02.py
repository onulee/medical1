import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://flight.naver.com/"


def compute_date(dates, target) -> list:
    print("compute entire date information from current month to limit")
    return [date for date in dates if date.text == str(target)]


browser = webdriver.Chrome()
# browser.maximize_window()

browser.get(URL)
time.sleep(1)

# remove AD popup
find = browser.find_elements(By.CLASS_NAME, "anchor")
for f in find:
    if f.get_attribute("title") == "지금 바로 혜택 확인하기":
        browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div/div[2]/button[1]').click()
        print("remove pop up")
        break

# push 가는 날 button also delay 1 sec is necessary, if don't use this, can not read date information.
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(1)

# read date information and push 25 day
dates = browser.find_elements(By.CLASS_NAME, "sc-evZas dDVwEk num".replace(" ", "."))
compute_date(dates, 25)[0].click()
# read date information and push 30 day
dates = browser.find_elements(By.CLASS_NAME, "sc-evZas dDVwEk num".replace(" ", "."))
compute_date(dates, 30)[0].click()


while True:
    pass
import oracledb
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 화면이 나타나는 것을 확인
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
# browser = webdriver.Chrome()
# browser.maximize_window()

# url = "https://www.melon.com/chart/index.htm"
# browser.get(url)
# time.sleep(2)

# selenium
# elem = browser.find_element(By.XPATH,'//span[text()=""]')
# browser.find_elements(By.XPATH,'//button[@class=""]')
# elem.click(), 
# elem.send_keys('시가총액')
# elem.send_keys(Keys.ENTER) 

# soup = BeautifulSoup(browser.page_source,"lxml")
# find,find_all

# 파일저장
# with open("melon.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())

# 파일불러오기
with open("melon.html","r",encoding="utf-8") as f:
    soup = BeautifulSoup(f,"lxml")

trs = soup.find_all("tr",{"id":"lst50"})
print("개수 : ",len(trs))

import requests
from bs4 import BeautifulSoup
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

url = "https://www.naver.com"

# 크롬브라우저 열기
browser = webdriver.Chrome()
# 네이버페이지 이동
browser.get(url)
time.sleep(2)

# 
elem = browser.find_element(By.XPATH,'//*[@id="shortcutArea"]/ul/li[6]/a')
elem.click()
time.sleep(2)
# 새로운 탭으로 이동
browser.switch_to.window(browser.window_handles[1])
elem = browser.find_element(By.XPATH,'//*[@id="container"]/div[2]/div/div[3]/a')
elem.click()
time.sleep(2)


# 완료
time.sleep(100)


    
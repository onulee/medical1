import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

# url= "https://www.naver.com"
url= "https://flight.naver.com/"

#브라우저 열기
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화
browser.get(url)

# 요소선택
# elem = browser.find_element(By.NAME,'query')
# elem.send_keys('네이버항공권')
# elem.send_keys(Keys.ENTER)

# elem = browser.find_element(By.CLASS_NAME,'link_name')
# elem.click()

# 네이버항공권 창으로 이동
# 원본창[0], 새창[1], 새창[2]
# browser.switch_to.window(browser.window_handles[1])

#-----------------------------------------
# 출발부분 클릭 - XPATH
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[1]/button[1]')
elem.click()
time.sleep(2)

# 국내 클릭 - CLASS_NAME사용, XPATH는 안됨.
elem = browser.find_element(By.CLASS_NAME,'autocomplete_Collapse__tP3pM')
elem.click()
time.sleep(2)

# 김포 클릭 - CLASS_NAME 복수 배열로 가져오기
elem = browser.find_elements(By.CLASS_NAME,'autocomplete_Airport__3_dRP')[2]
elem.click()

#-----------------------------------------
# 도착부분 클릭 - XPATH
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[1]/button[2]')
elem.click()
time.sleep(2)

# 국내 클릭 - CLASS_NAME사용, XPATH는 안됨.
elem = browser.find_element(By.CLASS_NAME,'autocomplete_Collapse__tP3pM')
elem.click()
time.sleep(2)

# 제주 클릭 - CLASS_NAME 복수 배열로 가져오기
elem = browser.find_elements(By.CLASS_NAME,'autocomplete_Airport__3_dRP')[1]
elem.click()
#-----------------------------------------
# 가는날짜 부분 선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[2]/button[1]')

time.sleep(2)












time.sleep(100)




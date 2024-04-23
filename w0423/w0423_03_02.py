from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

craw_keyword = input('크롤링할 키워드를 입력해주세요 : ')


options = Options()
options.add_experimental_option("detach", True)

# selenium으로 정보 가져오기
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()

driver.get("https://www.naver.com/")
time.sleep(2)

#검색창을 찾아 검색어 입력
driver.find_element(By.ID,'query').click()

element = driver.find_element(By.ID, 'query')

element.send_keys(craw_keyword)

#검색 버튼을 눌러 실행
driver.find_element(By.ID,'search_btn').click()

time.sleep(10)
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

# DB연결부분
# conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
# cursor = conn.cursor()
# sql = ""
# cursor.close()
# conn.close()

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()

# for i in range(5):
#     url = f"https://www.yeogi.com/domestic-accommodations?searchType=KEYWORD&keyword=%ED%98%B8%ED%85%94&checkIn=2024-06-05&checkOut=2024-06-06&personal=2&freeForm=true&page={i+1}"
#     browser.get(url)
#     time.sleep(2)

#     # text소스를 html소스로 파싱
#     soup = BeautifulSoup(browser.page_source,"lxml")

#     #### find_all()
#     hotels = soup.find_all("a",{"class":"gc-thumbnail-type-seller-card css-wels0m"})
#     print("전체 개수 : ",len(hotels))
#     title = hotels[0].find("h3",{"class":"gc-thumbnail-type-seller-card-title css-1asqkxl"})
#     print("제목 : ",title.text)

url = f"https://www.yeogi.com/domestic-accommodations?searchType=KEYWORD&keyword=%ED%98%B8%ED%85%94&checkIn=2024-06-05&checkOut=2024-06-06&personal=2&freeForm=true&page=1"
browser.get(url)
time.sleep(4)

# text소스를 html소스로 파싱
soup = BeautifulSoup(browser.page_source,"lxml")

#### find_all()
hotels = soup.find_all("a",{"class":"gc-thumbnail-type-seller-card css-wels0m"})
print("전체 개수 : ",len(hotels))

print(hotels[3])
import pandas as pd
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

movie_data = {}
year_list = []
title_list = []
viewer_list = []
rating_list = []

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()

# 년도별 year,title,viewer,rating 가져오기
for year in range(2019,2024):
    url = f"https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    browser.get(url)
    time.sleep(2)

    soup = BeautifulSoup(browser.page_source,"lxml")
    basic_list = soup.find("ul",{"class":"c-list-basic ty_flow35"})

    # 10개중 1개만 가져옴.
    movie_list = basic_list.find_all("li")
    for i,movie in enumerate(movie_list[0]):
        d_date = year
        print("년도 : ",d_date)
        d_strong = movie.find("strong",{"class":"tit-g clamp-g"})
        title = d_strong.find("a").text.strip()
        print("제목 : ",title)
        d_viewer = movie.find("p",{"class":"conts-desc clamp-g"})
        viewer = int(d_viewer.find("a").text.strip()[3:-2].replace(",",""))
        print("관객수 : ",viewer)
        
        # 평점 가져오기
        elem = browser.find_element(By.XPATH,'//strong[@class="tit-g clamp-g"]')
        time.sleep(1)
        elem.click()
        time.sleep(1)
        soup = BeautifulSoup(browser.page_source,"lxml")
        d_rating = soup.find("span",{"class":"gem-star-point"})
        rating = d_rating.find("span",{"class":"ico-pmp"}).nextSibling.strip()
        print("제목 : ",rating)
        
        # 데이터 저장
        year_list.append(year)
        title_list.append(title)
        viewer_list.append(viewer)
        rating_list.append(rating)
        
        browser.back()
        print("-"*50)

# dict저장
movie_data['year'] = year_list
movie_data['title'] = title_list
movie_data['viewer'] = viewer_list
movie_data['rating'] = rating_list
print(movie_data)
df = pd.DataFrame(movie_data)
print(df)

# 데이터 처리
# # list타입 저장
# list1 = []
# list1.append(10)
# list1.append(20)
# list1.append(30)
# list1.append(40)


# # dict타입 저장
# m_dict = {}
# m_dict['viewer'] = list1
# print(m_dict)
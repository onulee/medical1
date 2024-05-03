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

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()

# # 파일저장
# with open("daum_moive.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())

# 파일불러오기
# with open("daum_moive.html","r",encoding="utf-8") as f:
#     soup = BeautifulSoup(f,"lxml")

year = "2020"
# db저장
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()
for year in range(2020,2024):

    url = f"https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    browser.get(url)
    time.sleep(2)

    soup = BeautifulSoup(browser.page_source,"lxml")
    basic_list = soup.find("ul",{"class":"c-list-basic ty_flow35"})
    # print(movie_list)

    # 30개
    movie_list = basic_list.find_all("li")
    print(len(movie_list))
    for i,movie in enumerate(movie_list):
        print(f"[번호 {i+1}]")
        d_strong = movie.find("strong",{"class":"tit-g clamp-g"})
        title = d_strong.find("a").text.strip()
        print("제목 : ",title)
        img = movie.find("img")["src"]
        # 파일 저장
        with open(f"movie_{year}_{i+1}.jpg","wb") as f:
            d_img = requests.get(img)
            f.write(d_img.content)
        print("이미지 : ",img)
        d_audience = movie.find("p",{"class":"conts-desc clamp-g"})
        audience = int(d_audience.find("a").text.strip()[3:-2].replace(",",""))
        print("관객수 : ",audience)
        d_ddate = movie.find("span",{"class":"conts-subdesc clamp-g"})
        d_ddate = d_ddate.text.strip()[:-1]
        print("일자 : ",d_ddate)
        print("-"*50)
        
        # db저장
        # sql =f"insert into daum_movie values (movie_seq.nextval,'{title}','{img}',\
        # '{audience}','{d_ddate}')"
        
        sql = "insert into daum_movie values (movie_seq.nextval,:1,:2,:3,:4)"
        
        cursor.execute(sql,(title,img,audience,d_ddate))
        cursor.execute('commit')
   
print("종료")
cursor.close()
conn.close() 
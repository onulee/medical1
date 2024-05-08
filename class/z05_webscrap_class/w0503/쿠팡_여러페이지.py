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

page = 1
for page in range(1,4):
    url = f"https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={page}&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(url)
    time.sleep(2)

    soup = BeautifulSoup(browser.page_source,"lxml")

    ul_search = soup.find("ul",{"class":"search-product-list"})
    print("총 개수 : ",len(ul_search))
    # 모든 상품 검색
    lis = ul_search.find_all("li")
    # print("리스트 개수 : ",len(lis))
    conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
    cursor = conn.cursor()
    for i,li in enumerate(lis):
        print("[ ",i+1,"번째 상품 ]")
        
        print("li class : ",li["class"])
        # 왼쪽,오른쪽 공백제거
        title = li.find("div",{"class":"name"}).text.strip()
        print("제목 : ",title)
        img = li.find("img",{"class":"search-product-wrap-img"})["src"]
        # 파일 저장
        # with open(f"coupang_{i+1}.jpg","wb") as f:
        #     d_img = requests.get(img)
        #     f.write(d_img.content)
        print("이미지 : ",img)
        
        price = int(li.find("strong",{"class":"price-value"}).text.replace(",",""))
        print("가격 : ",price)
        if li.find("em",{"class":"rating"}) != None:
            grade = float(li.find("em",{"class":"rating"}).text)
            print("평점 : ",grade)
            eval_num = int(li.find("span",{"class":"rating-total-count"}).text[1:-1])
            print("평가인원수 : ",eval_num)
        else:
            grade = 0
            print("평점 : ",grade)
            eval_num = 0
            print("평가인원수 : ",eval_num)    
        print("-"*30)
        # db저장
        sql =f"insert into coupang values (coupang_seq.nextval,'{title}','{img}',\
        {price},{grade},{eval_num})"
        cursor.execute(sql)
        cursor.execute('commit')
    
    
input("프로그램 종료(Enter)")    


  
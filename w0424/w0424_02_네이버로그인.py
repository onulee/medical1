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
time.sleep(3)
# 로그인버튼 선택
elem = browser.find_element(By.CLASS_NAME,'MyView-module__link_login___HpHMW')
# 로그인버튼 클릭
elem.click()
time.sleep(random.randint(2,5))


# 제이쿼리 : $("#id").val(), 자바스크립트 : document.getElementById("id").value
# input_js = f'document.getElementById("id").value="{id}";
# document.getElementById("pw").value="{pw}";'           
# input_js = ''.format("aaa","1111")

# 자동화 방지를 위한 자바스크립트 활용 데이터 입력
input_js = 'document.getElementById("id").value="{id}"; \
            document.getElementById("pw").value="{pw}"; \
           '.format(id="aaa",pw="1111")
time.sleep(random.randint(2,5))
# 자바스크립트 명령어 실행
browser.execute_script(input_js)

          

# 아이디 입력창 선택
# elem = browser.find_element(By.ID,'id')
# 글자 입력
# elem.send_keys("aaa")
# time.sleep(random.randint(2,5))
# elem = browser.find_element(By.ID,'pw')
# elem.send_keys("1111")

time.sleep(random.randint(2,5))
elem = browser.find_element(By.CLASS_NAME,'btn_login')
time.sleep(random.randint(2,5))
# 로그인 버튼 클릭
elem.click()


# 완료
time.sleep(100)


    
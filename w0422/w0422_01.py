# 기본복사
import requests
from bs4 import BeautifulSoup
url = "https://browse.auction.co.kr/list?category=22160000"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url,headers=headers)
res.raise_for_status()

# 데이터 불러오기
soup = BeautifulSoup(res.text,"lxml")

# print(soup.find("div",{"id":"section--inner_content_body_container"}))
print(soup.find("div",{"class":"section--itemcard"}))

# print(soup.prettify())

# 파일저장
# with open("yeogi.html",'w',encoding='utf8') as f:
#     f.write(soup.prettify())


# print(soup.prettify())



import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
# print(res.text)
soup = BeautifulSoup(res.text,"lxml")
# 파일저장
# with open("test.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())

print(soup.title.text)  # soup 태그사용해서 text글자를 출력
print(soup.a)           # soup 태그사용
print(soup.a.attrs)     #soup a태그의 속성값 모두 출력
print(soup.a["href"])   # soup a태그 선택속성값 출력
# print(soup.find("div",attrs={"id":"footer"}))
print(soup.find("div",{"id":"footer"})) # soup에서 find 태그,속성 모두를 가지고 검색
# print(soup.div)
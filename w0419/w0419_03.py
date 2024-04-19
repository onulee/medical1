import requests
from bs4 import BeautifulSoup

# url = "https://www.coupang.com/"
url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

ul_search = soup.find("ul",{"class":"search-product-list"})

# 모든 상품 검색
lis = ul_search.find_all("li")
# print("리스트 개수 : ",len(lis))
for i,li in enumerate(lis[0:20]):
    print("[ ",i+1,"번째 상품 ]")
    # 광고상품 제외
    if "search-product__ad-badge" in li['class']:
        continue
    
    # 평점이 5.0 이상 - 실수형으로 변경 : 문자와 숫자 비교 에러
    if float(li.find("em",{"class":"rating"}).text) < 5.0:
        continue
    
    # 평가인원수가 200명이상 - 정수형으로 변경
    if int(li.find("span",{"class":"rating-total-count"}).text[1:-1]) < 200:
        continue
    
    print("li class : ",li["class"])
    # 왼쪽,오른쪽 공백제거
    print("제목 : ",li.find("div",{"class":"name"}).text.strip())
    print("가격 : ",li.find("strong",{"class":"price-value"}).text)
    print("평점 : ",li.find("em",{"class":"rating"}).text)
    # 평가인원수 200명 이상 출력하시오.
    print("평가인원수 : ",li.find("span",{"class":"rating-total-count"}).text[1:-1])
    print("-"*30)


  
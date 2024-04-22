# 기본복사
import requests
from bs4 import BeautifulSoup
url = "https://browse.auction.co.kr/list?category=22160000&k=31&p=1"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url,headers=headers)
res.raise_for_status()

# 데이터 불러오기
soup = BeautifulSoup(res.text,"lxml")

# print(soup.find("div",{"id":"section--inner_content_body_container"}))
section = soup.find("div",{"id":"section--inner_content_body_container"})

print("-"*40)
# print(section.find("div",{"class":"section--itemcard"}))
# 복수개 찾기 find_all
itemcards = section.find_all("div",{"class":"section--itemcard_info"})

print("개수 : ",len(itemcards))

for i,itemcard in enumerate(itemcards[0:10]):
    print("[",i+1,"번째 ]")
    print("제목 : ",itemcards[2].find("span",{"class":"text--title"}).text)
    price = int((itemcard.find("strong",{"class":"text__price-seller"}).text).replace(",",""))
    print("금액 : ", '{0:,}'.format(price) )
    
    # 후기평점,구매건수
    list_score = itemcard.find("ul",{"class":"list--score"})
    lis = list_score.find_all("li")
    # print("li 개수 : ",len(lis))
    if len(lis)==0:
        print("후기평점,구매건수 : 없음")
    elif len(lis) == 1:
        buycnt = int(lis[0].find("span",{"class":"text--buycnt"}).text[3:])
        print("구매건수 : ",buycnt)
    else: # li 3개가 있는 경우
        for_a11y = float(lis[0].find("span",{"class":"for-a11y"}).text[5:-1])
        print("후기평점 : ",for_a11y)        
        buycnt = int(lis[2].find("span",{"class":"text--buycnt"}).text[3:])
        print("구매건수 : ",buycnt)        
    
    print("-"*40)




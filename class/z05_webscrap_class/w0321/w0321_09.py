import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&q=%EB%93%B1%EC%B4%8C%EC%A3%BC%EA%B3%B5%20%EB%B6%84%EC%96%91&nzq=%EB%93%B1%EC%B4%8C%EC%A3%BC%EA%B3%B5&DA=RSJ"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# 등촌주공3단지 매매시세, 전세시세 출력하시오.
real = soup.find("ol",{"class":"list_place"})
li_list = real.find_all("li")

for i in range(len(li_list)):
    # print(len(li_list))
    title = li_list[i].find("div",{"class":"wrap_tit"}).a.text.strip()
    dd_list = li_list[i].find_all("dd",{"class":"f_red"})
    print("제목 : ",title)
    print("매매 시세 : ",dd_list[0].text)
    print("전세 시세 : ",dd_list[1].text)
    print("-"*50)




# with open("real.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())

print("종료")



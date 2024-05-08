import requests
from bs4 import BeautifulSoup
url="https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml") #text를 html파싱
# print(soup.prettify()) #html소스를 정렬해서 출력해 줌.

print("<title> : ",soup.title) #태그를 입력 태그정보 가져옴
print("<title> text : ",soup.title.get_text()) #태그의 글자를 가져옴.
print("<title> text : ",soup.title.text) #태그의 글자를 가져옴.
print("<a> 태그 : ",soup.a) 
print("<a> 태그글자 : ",soup.a.text)
print("<a> 속성전체 : ",soup.a.attrs) #태그의 속성값 모두 가져옴

print("<a>[1개속성] : ",soup.a["href"]) #대그의 1개 속성 가져옴.









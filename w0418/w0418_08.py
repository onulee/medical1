import requests
from bs4 import BeautifulSoup
url="https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# type_tr = soup.find("tr",{"class":"type1"})
# trs = type_tr.find_next_siblings("tr")
# print(trs[1].a['href'])

t_table = soup.find("table",{"class":"type_5"})
print(t_table.a['href'])



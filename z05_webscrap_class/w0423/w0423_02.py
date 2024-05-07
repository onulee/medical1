from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
from bs4 import BeautifulSoup as bs
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
def main():
    browser = webdriver.Chrome()
    url = "https://comic.naver.com/bestChallenge"
    browser.get(url)
    time.sleep(5) # 웹페이지 로딩 될 때까지 대기
    soup = bs(browser.page_source, 'lxml')
    with open('webtoons2.html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
        item_boxs = soup.find_all('div', 'component_wrap')[3]
        items = item_boxs.find_all('li', 'AsideList__item--i30ly')
        for item in items:
            title = item.find('span', 'ContentTitle__title--e3qXt').text
            img_url = item.find('img')['src']
            print('순위 :', item.find('strong', 'AsideList__ranking--sNPZy').text)
            print('제목 :', title)
            print('작가 :', item.find('a', 'ContentAuthor__author--CTAAP').text)
            print('이미지링크 :', img_url)
            img_poster = requests.get(img_url,headers=headers)
            with open('{}.jpeg'.format(title), 'wb') as f:
                f.write(img_poster.content)
                
if __name__ == '__main__':
    main()
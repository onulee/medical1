import requests
from bs4 import BeautifulSoup
# url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q=%EC%98%81%ED%99%94"

#---------
year_rate_sum = [0]*3 #년도별 평점 합계
year_rate_avg = [0]*3 #년도별 평점 평균
for y_i,y in enumerate(range(2021,2024)):
    url = f"https://search.daum.net/search?w=tot&q={y}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text,"lxml")

    movie_list = soup.find("ol",{"class":"movie_list"})
    # print(movie_list)

    # 30개
    
    m_list = movie_list.find_all("li")
    sum = 0
    for i,m in enumerate(m_list):
        if i == 5: break
        print(f"[번호 {i+1}]")
        print("-"*50)
        print("제목 : ",m.find("div",{"class":"info_tit"}).a.text)
        rate = float(m.find("em",{"class":"rate"}).text)
        sum += rate
        print("평점 : ",)
        img_screen = m.find("img")["data-original-src"]
        print(img_screen)
        # 이미지 저장부분
        # with open(f"movie_{y}_{i}.jpg","wb") as f:
        #     re_img = requests.get(img_screen) #url링크를 다시 읽어와야 함.
        #     f.write(re_img.content) # 파일이름의 내용을 저장
    print(f"{y}년도 평점합계 : ",sum)
    year_rate_avg[y_i] = float("{:.2f}".format(sum/5))
    year_rate_sum[y_i] = sum

#-------------


print("개수 : ",len(m_list))
print("년도별 평점합계 : ",year_rate_sum)
print("년도별 평점평균 : ",year_rate_avg)
print("종료")
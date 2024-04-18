import requests
res = requests.get("http://www.google.com")
# res = requests.get("http://www.naver.com")
res = requests.get("https://www.melon.com/chart")
print("응답코드 : ",res.status_code)    #Response [200] 정상출력 / 403 접근권한 없음
print(res)                                     #Response [200] 정상출력

if res.status_code == requests.codes.ok:
    print("정상출력")
else:
    print("접근을 할수 없습니다. [에러코드 : ",res.status_code,"]")

# res.raise_for_status()     #에러시 종료
# print("웹 스크래핑을 진행합니다.")   #종료가 되었기에 실행되지 않음.

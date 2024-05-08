import requests
# 웹에 접근해서 html소스를 가져옴.
res = requests.get("https://www.google.com/")
# res = requests.get("https://www.daum.net/")
#res = requests.get("https://www.melon.com/index.htm")
# 200 : 정상, 403,404 : 페이지없음  500: 프로그램에러
print(res) # 코드상태 출력
print("코드 : ",res.status_code) # 리턴한 소스의 코드값을 출력
print(type(res.status_code))
if res.status_code == requests.codes.ok: # requests.codes.ok : 200
    print("정상페이지 호출입니다.")
else:
    print("에러코드 발생")    

res.raise_for_status() # 코드가 200이 아니면 오류처리해서 자동 멈춤



print("-"*40)
# requests를 통해 html소스를 출력
print(res.text)





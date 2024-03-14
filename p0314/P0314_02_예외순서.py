# 외부와의 데이터 전송,데이터 받기,외부기기 연결, 다른 프로그램 연결
# 이런 곳 외에는 되도록 여러분이 프로그램이 오류 발생되지 않도록
# 하는게 가장 좋음.


print("프로그램 실행")
try:
    print(1)
    print(2)
    print(1/0) # 에러가 발생
    print(3)
except:    
    print(4)
    print(5)
print(6)
print("프로그램 종료")
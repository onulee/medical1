print("프로그램 실행")
try:
    print(1)
    print(2)
    # print(1/0) # 에러가 발생
    print(3)
except:    # 예외가 발생하면 실행
    print(4)
    print(5)
else: # 예외가 발생하지 않으면 실행
    print(6)    
        
print("프로그램 종료")
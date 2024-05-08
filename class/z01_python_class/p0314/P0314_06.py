a_list = [1,2,3]
try:
    print(a_list[5])
    print(1/0)
    txt = int(input("숫자를 입력하세요."))
    print(txt) 
except IndexError:
    print("리스트 주소가 잘못 입력되었습니다. ")    
except Exception as e:
    print("-- 예외가 발생했습니다.")
    print("타입 :",type(e))
    print(e)
    
    
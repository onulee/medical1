# 함수선언
def calc(v1,v2,op):
    result = 0 #지역변수
    if op == "1":
        result = v1+v2
    elif op == "2":
        result = v1-v2
    elif op == "3":
        result = v1*v2
    elif op == "4":
        result = v1/v2


aaa = 0 # 전역변수
print("1.더하기 2.빼기 3.곱하기 4.나누기")
a_input = input("계산하려고 하는 방식을 입력하세요.")        
var1 = int(input("첫번째 수를 입력하세요.>> "))
var2 = int(input("두번째 수를 입력하세요.>> "))

# 함수호출해서 return받음.
calc(var1,var2,a_input)
print("결과값 : ",result)                
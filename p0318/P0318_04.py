#키워드 매개변수, 키워드 매개변수는 제일 뒤에 와야 함.
def cal(num1=10,num2=10): 
    num1 = num1+10
    num2 = num2+20
    result = num1 + num2
    return result

# ---------------------------

num1 = 5
num2 = 7

result = cal() # 함수호출

print("현재 숫자 : ",num1, num2, result)
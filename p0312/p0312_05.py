# 지역변수의 리스트와 전역변수의 리스트
# 전역변수 리스트를 매개변수로 전달시 return 을 받지 않아도 됨.

# def multi(num1,num2,result_list):
#     result_list.append(num1+num2)
#     result_list.append(num1-num2)

# result_list = [] #전역변수
# num1 = int(input("숫자를 입력하세요.>> "))
# num2 = int(input("숫자를 입력하세요.>> "))
# multi(num1,num2,result_list)
# print("결과값 : ",result_list)

#------------------------------------------------
def multi(num1,num2):
    result_list = [] #지역변수
    result_list.append(num1+num2)
    result_list.append(num1-num2)
    return result_list

num1 = int(input("숫자를 입력하세요.>> "))
num2 = int(input("숫자를 입력하세요.>> "))
result_list = multi(num1,num2)
print("결과값 : ",result_list)
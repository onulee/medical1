def cal(input1,input2):
    result1 = input1+input2
    result2 = input1-input2
    result3 = input1*input2
    result4 = input1/input2
    return input1+input2,result2,result3,result4


input1 = int(input("1번째 숫자를 입력하세요.>> ")) 
input2 = int(input("2번째 숫자를 입력하세요.>> ")) 

# 함수의 return을 사용해서 입력된 두수의 사칙연산 결과값을 출력하시오.
# 20,10
# 결과값 : 30,10,200,2 

result1,result2,result3,result4 = cal(input1,input2)
data = cal(input1,input2)
print("더하기 : ",result1)
print("빼기 : ",result2)
print("곱하기 : ",result3)
print("나누기 : ",result4)
print("결과값 : ",result1,result2,result3,result4)
print("결과값 : ",data)
print("더하기 : ",data[0])




# for i in range(10):
#     sum = 0
#     sum += i
    
# for i in range(5):
#     result = 1
#     result += i
    
# print(sum)
# print(result)    
        



# def plus(v1,v2):
#     v1= v1+100 #101
#     v2= v2+200 #202
#     return v1,v2 #함수밖에서 사용하려면 return 값을 돌려줘야 함
    

# # 함수호출
# v1 = 1
# v2 = 2
# plus(v1,v2)

# # 출력
# print(v1,v2)    
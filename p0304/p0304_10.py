a = 10
b = a # 변수복사
b = 100
print(a) #값? 10
print(b) #값? 100

print("-"*40)

a_list = [1,2,3]
b_list = a_list #리스트복사
b_list[0] = 200
print(a_list[0]) #값? 
print(b_list[0]) #값? 200

# 대입 연산자
# == 
a = 3 # 3을 a에 넣는다.
a += 1 # a = a + 1
print(a)


a += 2 # a = a + 2
a += 100 # a = a + 100

# 더하기 뿐만 아니라 +=, -=, *=, /=, //=, %=, **= 산술연산자 모두 가능
# 즉, 좌변과 우변에 동일한 변수명이 사용될 경우,
# 변수명을 생략하고 축약시킬 수 있다.

a = 3
b = 2
a *= 2 + b 
# a = a*(2+b) 정답
# a = a*2 + b 오답
print(a) # 12

# num이 20에서 시작해서 값이 누적됨
num = 20
num += 2
print(num) # 22
num -= 2 # num = num - 2
print(num) # 20
num *= 2 # num = num *2
print(num) # 40
num /= 2 # num = num / 2
print(num) # 20 값은 계속 업데이트 된다...!!


 
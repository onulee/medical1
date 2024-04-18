# %d는 정수 %f는 실수 %s는 문자열!!
print("%d %f %s"%(10,12.3455,"문자"))
print("%.2f"%(12.3455)) # 소수 둘째자리까지 출력

#str.format()
print("문자열을 쓰고 {}".format(1))
# 정수
print("{0:d}".format(123))
print("{0}".format(123))
print("{}".format(123))

#실수
print("{0:f}".format(123.456789))
print("{0}".format(123.456789)) 
print("{}".format(123.456789))

#문자
print("{0:s}".format('문자'))
print("{0}".format('문자'))
print("{}".format('문자'))

print("{0} {1} {2}".format('빨','주','노'))
print("{0} {2} {1}".format("빨", "주","노"))

# 변수
number = 10
pi = 3.141592 
result = True
str1 = "문장입니다."
ch = "A"

s1 = '1+1=2'
print(s1)
s2 = '{}+{}={}'.format(1,1,2)
print(s2)

a = 100
a += 1 # a = a + 1 같은 표기
# +=, -=,*=, /=, //=, %=

a,b=1,2
a = 1
b = 2

print(a == b)
print(a != b)
print(a >= b)
print(a > b)

# 논리연산자
# and(둘 다 참이어야 함), or(둘 중에 하나만 참이어도 됨),
# not(참=>거짓, 거짓=>참)
a,b,c = 100,200,300
result = (a>c) and (b<c) # False
print(result)

r1 =  True
print( not r1 ) 

# 입력 받기 input
name = input("이름을 입력하세요:  ")
print("당신의 이름은 {}입니다.".format(name))
# input()의 결과 값은 문자형이다.
age = int(input("나이를 입력하세요:  "))
print("당신은 내년에 {}살 입니다.".format(age+1))


# if 조건문
# if 조건문1:
# 실행문1
# else:
#   실행문2:
# 조건문1이 참이면 실행문1을 실행 후 종료
# 조건문1이 거짓이면 실행문2를 실행 후 종료

f = "apple"
if f == "banana":
    print('먹는다')
else:
    print('먹지 않는다')
    



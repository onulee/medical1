# 문자열을 사용하여 프린트로 출력하기
str1 = "name"
print("이름을 영어로 하면 무엇일까요?", str1)

# 프린트 시 문자열을 중간에 삽입하는 방법
str2 = "jane"
print('나의 이름은 %s 입니다.'%str2)
print('나의 이름은',str2+'입니다.')
print('나의 이름은 {}입니다.'.format(str2))

# 정수형 입력
num1 = 10
num2 = 100
print(num1, num2)
print(num1+num2)

# 정수 계산 시 print 내 사칙 연산이 가능하다.
num1 = 20
num2 = 200
num3 = 2000
print("%d + %d + %d = %d"%(num1, num2, num3, num1+num2+num3))

# 실수타입이 있을 때
num4 = 10
num5 = 100.3
num6 = 1000
print("%d+%.1f+%d=%.1f"%(num4,num5,num6,num4+num5+num6))

print("{}+{}+{}={}".format(num4,num5,num6,num4+num5+num6))
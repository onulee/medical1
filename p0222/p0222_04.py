# 두 수를 입력 받아서 사칙연산을 출력해보세요
# 변수 n1, n2
# 10 + 3 = 13
# 10 - 3 = 7
# 10 * 3 = 30
# 10 / 3 = 3.333

num1 = int(input("첫 번째 숫자를 입력해주세요:  "))
num2 = int(input("두 번째 숫자를 입력해주세요:  "))

print('{} + {} = {}'.format(num1,num2,num1+num2))
print('{} - {} = {}'.format(num1,num2,num1-num2))
print('{} * {} = {}'.format(num1,num2,num1*num2))
print('{} / {} = {}'.format(num1,num2,num1/num2))

# 해보세요
cal = input('수식을 입력하세요(+,-,*,/):  ')
n1 = int(input("첫 번째 숫자를 입력해주세요:  "))
n2 = int(input("두 번째 숫자를 입력해주세요:  "))

if cal == '+':
    print("{} + {} = {}".format(n1,n2,n1+n2))
elif cal == '-':
    print('{} - {} = {}'.format(n1,n2,n1-n2))
elif cal == '*':
    print('{} * {} = {}'.format(n1,n2,n1*n2))
elif cal == '/':
    print('{} / {} = {}'.format(n1,n2,n1/n2))
else:
    print("[ 올바르지 않은 수식을 입력하였습니다.]")
    print("[ 다시 입력해주세요.]") 

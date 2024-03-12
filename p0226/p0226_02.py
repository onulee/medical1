# 해보세요
# 1. 나이가 10살 이상이고 150 이상만 탑승가능
# 나이, 키를 입력받아
# [탑승 가능] [탑승 불가능]을 출력해보세요

age = int(input("나이를 입력하세요:  "))
height = float(input("키를 입력하세요:  "))

if age >= 10:
    if height >= 150:
        print(" [ 놀이기구 탑승가능 ]")
    else:
        print("[ 놀이기구 탑승 불가능 ]") # 나이는 10살 이상이나 키 미달
else:
    print("[ 놀이기구 탑승 불가능 ]")


# 2. 숫자 3개 (정수)를 입력받고, 연산 1개를 입력받아
# +++, ---, ***, ///(나누기 값은 소수 둘째자리가까지 표현)
# a + b + c = d의 형태로 출력 (1+2+3=6)
# 숫자 3개로 계산기

n1 = int(input("첫 번째 숫자 입력:  "))
n2 = int(input("두 번째 숫자 입력:  "))
n3 = int(input("세 번째 숫자 입력:  "))

choice = input("연산을 고르세요:  ")

if choice == '+':
    result = n1+n2+n3
    print("{} + {} + {} = {}".format(n1,n2,n3,result))
elif choice == '-':
    result = n1-n1-n3
    print("{} - {} - {} = {}".format(n1,n2,n3,result))
elif choice == '*':
    result = n1*n2*n3
    print("{} * {} * {} = {}".format(n1,n2,n3,result))
elif choice == '/':
    result = n1/n2/n3
    print("{} / {} / {} = {:.2f}".format(n1,n2,n3,result))
else:
    print('잘못 입력하셨습니다.')

# print('{},{},{}의 연산 값은 {}'.format(n1,n2,n3,result)) 라고 입력해도됨


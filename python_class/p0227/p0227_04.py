''' 
반복문 - for, while
for 변수 in 반복가능한 데이터:
    수행문
    
for 카운터 변수 in range(시작값, 끝값+1, 증감값) :
    수행문
'''
for i in range(0,10,1): # 0,1,2,3,4,5,6,7,8,9 10번 반복
    print(i,'증감 1: 수행문입니다.')
    
for i in range(0,10,2):  # 0,2,4,6,8
    print(i,'증감 2: 수행문입니다.')

for i in range(0,3):  # 증감값이 1일 때는 생략이 가능
    print('두 번째 수행문입니다.')
    
for i in range(5):  # 5번 반복해라
    print('세 번째 수행문입니다.')

print('-'*35)
for i in range(3): # 3번 반복해라 1 증가 생략, 0부터 생략
    print(i)

# 카운터 변수 i를 사용하지 않을 때 _로 사용이 가능하다.
for _ in range(7): # 안녕하세요 7번 반복하세요
    print('안녕하세요')
    
for i in range(10,0,-2):
    print(i,'증감 2: 수행문입니다.')
    
l1 = [100,200,300,400,500]
#      0   1   2   3   4
# 리스트 안 요소확인 in / not in
'''
for 변수 in 리스트명:
    실행문
    
for 변수 in range(len(리스트명))
     실행문
     리스트명[변수]
'''
for n in l1:
    print(n)
    
for i in range(len(l1)):
    print(i)   # 0,1,2,3,4 ...
    print(l1[i])  # l1[0],l1[1],l1[2],....

# for문을 사용해서 1-100 사이의 홀수를 출력해보세요
# 1) if 사용하지 않음 (증감이용)
for i in range(1,101,2):
    print(i, end=' ')
print()  # 줄바꿈
# 2) if 사용
for i in range(1,101):
    if i%2 == 1:
        print(i, end=' ')
print()
# 50 에서 1 사이의 6의 배수를 역순으로 출력해보세요
# 1) if 사용하지 않음 (증감이용)
for i in range(48,0,-6):
    print(i, end=' ')
print()
# 2) if 사용
for i in range(50,0,-1):
    if i%6 == 0:
        print(i, end=' ')
print()

# input() 사용
# 입력 : 두 개의 숫자를 입력받음
# 출력 : 사칙연산
     # a + b = c
     # a - b = c
     # a * b = c
     # a / b = c
# 계산을 10번 반복하는 코드를 만드세요
for i in range(2):
    print([ i+1 ])
    num1 = int(input('첫 번째 숫자:  '))
    num2 = int(input( '두 번째 숫자:  '))
    print('[ {} + {} = {} ]'.format(num1,num2,num1+num2))
    print('[ {} - {} = {} ]'.format(num1,num2,num1-num2))
    print('[ {} * {} = {} ]'.format(num1,num2,num1*num2))
    print('[ {} / {} = {:.2f} ]'.format(num1,num2,num1/num2))
print()

for i in range(2):
    print([ i+1 ])
    n1 = int(input('첫 번째 숫자:  '))
    n2 = int(input('두 번째 숫자:  '))
    ch = input('연산자 선택:  ')
    if ch == "+":
        print('[ {} + {} = {} ]'.format(n1,n2,n1+n2))
        print()
    elif ch == '-':
        print('[ {} - {} = {} ]'.format(n1,n2,n1-n2))
        print()
    elif ch == '*':
        print('[ {} * {} = {} ]'.format(n1,n2,n1*n2))
        print()
    elif ch == '/':
        print('[ {} / {} = {:.2f} ]'.format(n1,n2,n1/n2))
        print()
    else:
        print('해당하는 연산값을 도출해낼 수 없습니다.')
print()
# 반복문 for문, while문
'''
for i in range(시작, 끝+1, 증감값):
    수행할 문장
    
while 조건식: # 이 조건이 참일 때
    실행할 문장

변수 =  시작값  # ex) i = 0
while 변수 < 끝값 : # 이 조건이 참일 때
    반복구문
    변수 = 변수 + 증가값  # i = i + 1
 '''
 
# for 문으로 안녕하세요를 3번 출력
for i in range(3):
    print('안녕하세요')

 # while문으로 작성
i = 0
while i < 3 :
    print('while : 안녕하세요')
    i = i + 1
    
# for 문으로 0 - 10까지 출력
for i in range(11):
    print(i, end=' ')
print()
# while 문으로 0 - 10까지 출력
i = 0
while i < 11 :
    print(i, end=' ')
    i += 1
print()
    
# while 을 사용해서 
# 해보세여
# 1 - 10 사이의 3의 배수를 출력해보세요:
j = 1
while j < 11:
    if j % 3 == 0:
        print(j, end= ' ')
    j += 1
print()
# 1 - 100 사이의 홀수를 출력
k = 1
while k < 101:
    if k % 2 == 1:
        print(k, end=' ')
    k += 1
print()
# 1 - 100까지의 합을 구해보세요
sum = 0
for i in range(1,101):
    sum += i
print(sum)

sum1 = 0
h = 0
while h < 101:
    sum1 += h
    h = h + 1
print(sum1)

# while True: # 무한히 반복시키고자 할 때 사용
#     print('ㅋ', end=' ')
# while 조건문이 참인경우 반복
# 때문에 while True는 무조건 참이기 때문에 무한히 반복된다.
# 무한루프에 들어가면 ctrl+c를 눌러서 강제종료할 수 있다.

# while문을 사용할 때 조건문을 잘 만드는게 중요하다.
# while 1 == 1:
#     print('ㅋ',end=' ')

# break, continue
# break 반복문을 빠져나와서 다음단계를 수행한다.
n = 0 
while n < 100:
    print(n, end=' ') # n = 0 n =1 n = 2
    if n == 4 :
        break
    n =  n + 1
    print('--------------')

breakletter = input('중단할 문자를 입력하세요:  ')
for letter in 'python':
    if letter == breakletter:
        break
    print(letter)

while True:
    n = input('숫자를 입력해주세요:  ')
    print(n)
    if n == '0' :
        print('종료되었습니다.')
        break
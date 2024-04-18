# 반복문
'''
for 변수 in range(시작값, 끝값+1, 증가값): 
'''
for i in range(3):
    print('안녕')
# i = 0 일때
# i = 1 일때
# i = 2 일때

for i in range(3): # i = 0, 1, 2
    print(i)

# i = 0,1,2,3...
# i = 1,2,3,4,5...
for i in range(100):
    print(i+1)
    
sum1 = 0
for i in range(1,6,1):
    sum1 = sum1 + i

# 숫자 한 개를 입력받아서 1부터 입력한 수 까지의 합을 구하세요
sumn = 0
num = int(input("n까지의 합:  "))
for i in range(1,num+1,1):
    sumn += i
print('1부터 {}까지의 합: {} '.format(num,sumn))

# 위의 코드에서 짝수의 합만 구하도록 코드 짜기
sumn1 = 0
SUM = []
n1 = int(input('n까지 짝수의 합, n:  '))
for i in range(1,n1+1):
    if i % 2 == 0:
        SUM.append(i)
        sumn1 += i
print(SUM)
print('1부터 {}까지의 짝수 합: {}'.format(n1,sumn1))

# 1-10까지의 곱
multi = 1
m1 = int(input('n까지의 곱, n:  '))
for i in range(1,m1+1):
    multi *= i
print('1에서부터 {}까지의 곱 : {}'.format(m1,multi))


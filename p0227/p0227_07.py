# 1 - 5까지의 합계를 구하세요
t = 0
for i in range(1,6,1):
    t = t + i
print(t)  

a = 0
for i in range(1,6,1):
    a += i
print(t)

total = 0
total = total + 1 # t = 1
total = total + 2 # t = 1 + 2
total = total + 3 # t = 1 + 2 + 3 ...
total = total + 4 
total = total + 5
print(total)

# 1에서 10까지의 합을 구해보세요
sum10 = 0    # 변수 초기화
for i in range(1,11):
    sum10 += i
print('1부터 10까지의 합은 {}입니다.'.format(sum10))

 # 1 에서 100까지의 합을 구해보세요
sum100 = 0     # 변수 초기화
for i in range(1,101):
    sum100 += i
print('1부터 100까지의 합은 {}입니다.'.format(sum100))

# 입력한 수부터 입력한 수까지의 합을 구해보세요!
num = 0
n1 = int(input('시작 숫자:  '))
n2 = int(input('끝 숫자:  '))
for i in range(n1,n2+1,1):
    num += i
print('{}부터 {}까지의 합은 {}입니다.'.format(n1,n2,num))

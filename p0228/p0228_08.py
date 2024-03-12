# 중첩 for
# for 안에 for
for i in range(3):  # i = 0,1,2
    print('i = ',i)
    for j in range(2): # i = 0,1
        print('j = ',j)

# for문을 사용해서 2단을 출력
for i in range(2,10):
    for j in range(1,10):
        print('{} * {} = {}'.format(i,j,i*j))
    
# 입력 받은 숫자의 단을 출력하세요 
num = int(input("단을 입력하세요:  "))
for i in range(1,10):
    print('{} * {} = {}'.format(num,i,num*i))
    
# 출력 형태
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
for j in range(6):
    print(j+1,'번째 출력')
    for i in range(1,6): # i = 1 2 3 4 5
        print(i,end=' ') # 1 2 3 4 5를 한줄로 출력
    print() # 줄바꿈
print('for문 끝')

for i in range(2,10):
    print('[',i,'단 ]')
    for j in range(1,10):
        print('{} * {} = {}'.format(i,j,i*j), end=' ')
    print()
    
# 짝수단, 홀수단만 출력해보세요
for i in range(1,10):
    for j in range(2,10):
        if j % 2 == 0:
            print('{}*{}={}'.format(j,i,i*j),end='\t')
    print()
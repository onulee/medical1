from random import *

n1 = randrange(1,10) # 1 - 9 사이의 정수
n2 = randrange(10) # 0 - 10 사이의 정수
n3 = randint(1,10) # 1 - 10 사이의 정수

print(n1,n2,n3)

lotto = []
# lotto에 1-10사이의 랜덤한 숫자 6개를 넣어보세요
for i in range(6):
    n1 = randint(1,45)
    lotto.append(n1)
print('6개의 랜덤 숫자: {}'.format(lotto))

mynum = []
# 내가 직접 입력한 숫자 6개를 넣어보세요
for n in range(6):
    n2 = int(input('숫자를 입력하세요:  '))
    mynum.append(n2)
print('내가 선택한 6개의 숫자: {}'.format(mynum))

if lotto == mynum:
    print('로또 1등 당첨')
else:
    print(('낙첨 입니다.'))
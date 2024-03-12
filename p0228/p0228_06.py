from random import *

# n = randrange(1,11) # 1 - 10까지의 정수
# n2 = randint(1,10) # 1 - 10까지의 정수

# 랜덤한 숫자 6개 lotto 리스트에 넣고
# 내가 입력한 숫자 6개는 mynum 리스트에 넣어주세요
# 1. 변수 선언
lotto = []
mynum = []
# 2. 숫자 6개 입력받기 (내가 입력한 숫자 6개는 mynum 리스트에)
for i in range(6):
    n = int(input("{}번째 숫자를 입력해주세요 >>".format(i+1)))
    mynum.append(n)
# 3. 로또 숫자 생성(랜덤한 숫자 6개 lotto 리스트에 넣고)
# 중복없이 숫자를 입력받고 싶다.
for i in range(6):
    tmp = randint(1,10)
    if tmp not in lotto:  # 만약에 랜덤숫자(tmp)가 lotto리스트에 없다면
        lotto.append(tmp)  # 추가해라

# 4. 입력 숫자와 랜덤숫자 비교
print('lotto 숫자는 {}입니다.'.format(lotto))
print('내가 고른 숫자는 {}입니다.'.format(mynum))

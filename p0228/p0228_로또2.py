from random import *

# 1. 1 - 45 까지의 숫자를 넣어서
l = []
for i in range(1,46,1):
    l.append(i)

# 2. 입력을 1-45 사이의 숫자를 입력 받음(6개)
mynum_bonus = []
mynum = [] 
for i in range(6):
    print('* {}번째 숫자'.format(i+1))
    num = int(input("숫자를 입력하세요:  "))
    mynum.append(num)
bonus = int(input("보너스 번호를 입력하세요:  "))
mynum_bonus.append(mynum)
mynum_bonus.append(bonus)
print('선택한 번호 = {}, 보너스 번호 ={}'.format(mynum_bonus[0],mynum_bonus[1]))

# 3. 1-45사이의 랜덤한 숫자 6자리 저장
lotto_bonus = []
lotto = []
for i in range(200):
    tmp = randint(0,44)
    l[0],l[tmp] = l[tmp],l[0]
for i in range(6):
    lotto.append(l[i])
lotto_bonus.append(lotto)
lotto_bonus.append(l[6])
print('로또 번호 = {}, 보너스 번호 = {}'.format(lotto_bonus[0],lotto_bonus[1]))

# 4. 입력숫자와 랜덤숫자 비교
count = 0
right = []
for i in lotto:
    if i in mynum:
        count += 1
        right.append(i)

# 5. 출력
print("일치하는 개수: {}".format(count))
print("일치하는 숫자: {}".format(right))


# 6. 등수
if count == 6:
    print("로또 1등 당첨입니다.")
elif count == 5 and lotto_bonus[1] == mynum_bonus[1]:
    print("로또 2등 당첨입니다.")
elif count == 5:
    print("로또 3등 당첨입니다.")
elif count == 4:
    print("로또 4등 당첨입니다.")
elif count == 3:
    print("로또 5등 당첨입니다.")
else:
    print("낙첨입니다.")
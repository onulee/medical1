from random import *
# 랜덤한 숫자를 만들어서 (1-100 사이)
# 내가 입력한 값이 랜덤한 숫자랑 같으면 당첨(프로그램 종료.)
# 아니면 다시입력해주세요
# 를 출력하는 프로그램을 만들어보세요!!!
'''
while True:
    lotto = randint(1,45)
    # print('행운의 숫자: {}'.format(lotto)) 당첨된 숫자를 알 수 있음
    num = int(input("원하시는 숫자를 입력해주세요:  "))
    if num == lotto:
        print("당첨입니다!")
        break
    else:
        print('다시 입력해주세요')
print('프로그램 종료.. 당첨금을 수령하세요!')
'''
# 입력한 숫자가 랜덤숫자보다 작으면 작습니다. 더 큰수를 입력해주세요
'''
randNum = randint(1,45)
while True:
    mynum = int(input("원하시는 숫자를 입력해주세요:  "))
    if randNum == mynum:
        print('당첨입니다!')
        break
    elif randNum > mynum:
        print('입력한 숫자가 랜덤숫자보다 작습니다. 다시 입력해주세요.')
    else:
        print('입력한 숫자가 랜덤숫자보다 큽니다. 다시 입력해주세요.')
print('프로그램 종료... 당첨금을 수령하세요!')
'''

# 1. 현재 입력한 숫자 모두를 inputlist에 넣으세요
inputlist = []
# 2. 10회 도전 후 프로그램이 종료가 되게 해주세요
rl = randint(1,45)
# print(rl)
while True:
    mm = int(input("원하시는 숫자를 입력해주세요:  "))
    if mm == rl :
        print('당첨입니다!')
        break
    else:
        inputlist.append(mm)
        if len(inputlist) == 10:
            print('10회 입력을 초과하였습니다.')
            # 3. 10회 도전에 실패한 사람에게 랜덤숫자 알려주기
            print('행운의 숫자는 [ {} ]'.format(rl))
            break
print('---- 프로그램 종료 ----')

# 또는..
cnt = 0
while cnt < 10:
    cnt += 1

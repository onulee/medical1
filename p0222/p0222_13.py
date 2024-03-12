# 1. 숫자를 입력받아서 양수면 양수 아니면 음수를 출력  if else
n = int(input("숫자를 입력하세요 >> "))

if n > 0:
    print('입력하신 숫자 {}는 양수입니다'.format(n))
else:
    print('음수입니다')

# 2.숫자가 0입니다 0이 아닙니다 if-else

if n == 0:
    print('0 입니다')
else:
    print('0이 아닙니다.')
# while문과 if문 사용
# 숫자 두개를 입력받고, (input)
# 연산자를 입력받아서 (+,-,*,/) (input)
# 무한히 계산하는 계산기를 만드는데 (while True)
# 첫번째 숫자에 0을 입력하면 프로그램이 종료가 되는 코드를 만드세요
# break
# while 조건식: # 조건식이 참일때 실행문 수행
#                즉 조건식이 거짓일 때 종료
# 실행문
while True:  
    n1 = int(input('첫 번째 숫자 입력:  '))
    if n1 == 0:
        print('종료되었습니다.')
        break
    n2 = int(input('두 번째 숫자 입력:  '))
    s = input('연산자 입력:  ')
    if s == '+':
        print('{} + {} = {}'.format(n1,n2,n1+n2))
    elif s == '-':
        print('{} - {} = {}'.format(n1,n2,n1-n2))
    elif s == '*':
        print('{} * {} = {}'.format(n1,n2,n1*n2))
    elif s == '/':
        print('{} / {} = {:.2f}'.format(n1,n2,n1/n2))
    else:
        print('연산을 잘못 선택하셨습니다. 다시 선택해주세요 >>')
print('프로그램이 종료되었습니다.')
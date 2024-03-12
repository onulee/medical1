# n1단부터 n2단까지 출력하세요
n1 = int(input('첫 번째 숫자 입력:  '))
n2 = int(input('두 번째 숫자 입력:  '))

if n1 > n2:
    n1, n2 = n2, n1
    print('{}단부터 {}단까지'.format(n1,n2))
for i in range(1,10):
    for j in range(n1,n2+1):
        print('{}*{}={}'.format(j,i,i*j), end='\t')
    print()
           
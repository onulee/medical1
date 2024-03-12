print('2단 출력')
for i in range(1,10): # 1,2,3,4,5,..9
    print('2 * {} = {} '.format(i,2*i))
for i in range(1,10):
    print('{} * {} = {} '.format(2,i,2*i))
    
# 원하는 단을 입력받아서 구구단을 입력하세요
# 3단을 입력받으면 3단 출력
for m in range(10):
    print('[',str(m+1)+'차례 ]')
    num = int(input("원하는 구구단을 입력하세요:  "))
    print('{}단 출력'.format(num))
    for i in range(1,10):
        print(' {} * {} = {} '.format(num,i,num*i))
    print('-'*35)
    
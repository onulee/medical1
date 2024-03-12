numL = []

# 0에서부터 5까지 넣어보세요
# append
numL.append(0)
numL.append(1)
numL.append(2)
numL.append(3)
numL.append(4)
numL.append(5)
print(numL)

# for문을 사용하여 0-5까지 숫자 넣기
num = []
for i in range(6): # i는 0에서부터 6미만까지 1씩 증가하여 []안으로 첨가
    num.append(i)
    
print('num[] = ',num)

aa = [1,2,3,4]
# index 를 사용하여 값 읽기
for i in aa:
    print(i)
    
for i in range(0,4):
    print(aa[i])

f = ['사과','복숭아','딸기','포도','자몽']
for i in f:
    print(i)
for i in range(0,len(f)): # 리스트의 길이 len함수는 반복문에서 많이 사용된다. 
    # len(f): f그룹 내 자료의 개수를 나타내줌 = range(0,5)
    print(f[i])
    
c = ['미국','영국','호주','캐나다','일본','중국']
# for문을 사용해서 하나씩 떼어서 출력해보기 (2가지 방법)
for i in c:
    print(i)
for i in range(0,len(c)):
    print(c[i])

# 1에사 100까지 들어가는 numL=[]를 만들고 출력해보기
numL = []
for i in range(100):
    numL.append(i+1)
    # print(i+1, end=' ') # 출력 확인
print('numL[] =',numL)
for i in range(100):
    print(numL[i])
    
# 반복문 안에 if문 사용
for i in range(10):
    print(i) # 0 ~ 9 까지 출력이 됨
    if i == 9:
        print('9 입니다.')
        
lan = ['영어','스페인어','일본어','중국어']
for i in lan:
    if i == '영어':
        print('영어입니다.')
    else:
        print('다른 언어입니다.')
        
# 2의 배수만 출력 (1-100 사이)
# 1. 증감 사용
for i in range(2,102,2):
    print(i, end=' ')

# 2. if 사용
for i in range(100):
    if (i+1)%2 == 0:
        print(i+1, end=' ') # ' '을 간격으로, 1 ~ 100까지 출력
for i in range(1,101):
    if i%2 == 0:
        print(i, end=' ') # 1 ~ 100 까지 출력

# 7의 배수만 출력 (1-100 사이)
# 1. 증감 사용
for i in range(7,100,7):
    print(i, end=' ')

# 2. if 사용
print()
for i in range(100):
    if (i+1)%7 == 0:
        print(i+1, end=' ')
        
print()
for i in range(1,100):
    if i%7 == 0:
        print(i, end=' ')
print()

aa = [100,90,86,79,72,52,98,94]
for a in aa:
    if a >= 80:
        print(a,'합격')

# 딸기가 있으면 딸기, 다른 과일은 다른과일이라고 출력
f = ['사과','복숭아','딸기','포도','자몽']
for i in f:
    if i == '딸기':
        print('딸기')
    else:
        print('다른 과일입니다.')

# 짝수면 짝수, 홀수면 홀수를 출력
num = [1,2,5,7,9,10,23,43]
# 1. for i in num:
for i in num:
    if i % 2 == 0:
        print('짝수')
    else:
        print('홀수')
# 2. for i in range(len(num)):
for i in range(len(num)):
    # print(i) i : 0, 1, 2, 3, ...
    # range(len(num)) = range(8) 8번 반복 -> 0,1,2,3,4,5,6,7
    # print(num[i]) -> num[0], num[1], num[2], ....
    if num[i]%2 == 0:
        print(num[i],'짝수')
    else:
        print(num[i],'홀수') # num=[]의 자료와 관계 없이...차례대로 0~7의 값이기 때문에 짝홀짝홀짝홀짝홀
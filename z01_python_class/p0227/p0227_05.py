
# 0 - 20 사이의 5의 배수로 이루어진 리스트를 만들어보세요!
# 출력 : [0,5,10,15,20]

numL = []
for i in range(0,21,5):
    # print(i, end=' ')
    numL.append(i)
print(numL)  # for 문에 들어가 있으면, 숫자 하나하나가 들어가는 대로 리스트를 나타낸다
# 또는
for i in range(21):
    if i % 5 == 0:
        numL.append(i)
print(numL)

lan = ['c','python','java','jquery','css']

# 1. 하나하나 출력해보기
# 1) 리스트명 사용
for i in lan:    
    print(i)
# 2) in range(len()) 사용
for i in range(len(lan)):
    print(lan[i])
# 2. 카운터변수 i 사용해서
#    1. c   
#    2. python
#    3. java ...형태로 출력
for i in range(len(lan)):
    print(str(i+1)+'.', lan[i])


num = [1,-1,2,3,-4,5,6,-8,9,-10]
# 양수면 양수, 음수면 음수 출력
for i in range(len(num)):
    if num[i] > 0:
        print('{} : 양수'.format(num[i]))
    elif num[i] < 0:
        print('{} : 음수'.format(num[i]))
    else:
        print('0 입니다.')
        
for n in num:
    if n > 0:
        print('{} : 양수'.format(n))
    elif n < 0:
        print('{} : 음수'.format(n))
    else:
        print('0 입니다.')
  

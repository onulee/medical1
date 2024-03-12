# 1. 변수 선언
score = [
    [80,90,85], [70,80,90], [84,92,80],[72,81,76]
]
name = ['홍길동','유관순','이순신','김구']
total = []
# 2. 코딩
# 2 - 1) 요소 하나하나 출력해보세요 80 90 85 70 80 90 ...
for i in range(len(score)):
    for j in range(len(score[i])):
        print(score[i][j], end=' ')

# 2 - 2) 작은 요소의 합을 구해서 total에 넣어주세요
#        total = [255,240,256,229]
'''
sum1,sum2,sum3,sum4 = 0,0,0,0
for j in range(len(score[0])):
    sum1 += score[0][j]
total.append(sum1)
for j in range(len(score[1])):
    sum2 += score[1][j]
total.append(sum2)
for j in range(len(score[2])):
    sum3 += score[2][j]
total.append(sum3)
for j in range(len(score[3])):
    sum4 += score[3][j]
total.append(sum4)
'''

for i in range(len(score)):
    s = 0
    # print(score[i])
    # i = 0, score[0][0] + score[0][1]+score[0][2] = s
    # i = 1, score[1][0] + score[1][1]+score[1][2] = s
    # i = 2, score[2][0] + score[2][1]+score[2][2] = s
    for j in range(len(score[i])):
        s += score[i][j]
    total.append(s)
            
print()  # 줄바꿈
print('score = {}'.format(score))
print('각 요소들의 합 = {}'.format(total))

# 3. 출력
for i in range(len(total)):
    if total[i] >= 250:
        print('{}님 합격입니다.'.format(name[i]))
    else:
        print('{}님 불합격입니다.'.format(name[i]))
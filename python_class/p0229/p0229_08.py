# 1 - 100까지 더하는데
# 총합이 100이 넘었을 때 수를 출력하세요
# 1 + 2 + ...

sum = 0
n = 0
while n < 100:
    n += 1
    sum += n
    if sum > 100:
        print('총합 : {}'.format(sum))
        break
print('수 {}'.format(n))

sum1 = 0
for i in range(101):
    i += 1
    sum1 += i
    if sum1 > 100:
        print('총합: {}'.format(sum1))
        break
print('프로그램 종료')


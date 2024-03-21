# continue 예제
# 1 - 100 합계를 구하는데 3의 배수는 제외하고 더하기
# while or for 사용해서!!
# 3의 배수를 제외하고 1-100사이의 값
i = 0
while i < 100:
    i += 1
    if i % 3 == 0:
        continue
    print(i,end=' ')
print()

# 1-100까지 출력,3의 배수는 제외하고
# 1) while 문
sum = 0
i = 0
while i < 100:
    i += 1
    if i % 3 == 0:
        continue
    sum += i
print('1-100사이의 3의 배수를 제외하고 더한 수의 값: {}'.format(sum))
print()
# 2) for문
sum1 = 0
for j in range(1,101):
    if j % 3 == 0:
        continue
    sum1 += j
print(sum1)
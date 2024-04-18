num = []
# for문을 사용해서 1-10까지 숫자를 num에 채우세요
for i in range(1,11,1):
    num.append(i)
print('num[] =',num)


num2 = []
# 1-10까지의 짝수를 num2리스트에 넣으세요
for n in range(1,11,1):
    if n % 2 == 0:
        num2.append(n)
print('num2[] =',num2)
# num1 = [i for i in range(1,11)] 이렇게 한줄로도 표현할 수 있다.

# 1~10까지의 합 for문을 사용해서 구할 수 있음.
# num = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for m in range(len(num)):
    sum += num[m] 
print('num 리스트 내의 합은: {}'.format(sum))

# num2 리스트 내의 합
sum2 = 0
for a in range(len(num2)):
    sum2 += num2[a]
print('num2 리스트 내의 합은: {}'.format(sum2))
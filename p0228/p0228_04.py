# 1 - 100까지의 합
n = 0
for i in range(1,101):
    n += i
print('1에서부터 100까지의 합은 {}'.format(n))

# 1 - 100까지의 짝수들의 합
m = 0
o = 0
for j in range(1,101):
    if j % 2 == 0:
        # print(j, end=' ')
        m += j
    else:
        # print(j, end=' ')
        o += j
print("1에서부터 100 사이의 짝수들의 합은 {}".format(m))
print("1에서부터 100 사이의 홀수들의 합은 {}".format(o))

# 1. 1 - 10 까지의 합
n1 = 0
for i in range(1,11):
    n1 += i
print(n1)

# num 리스트 안에 있는 값들의 합
num = [1,2,3,4,5,6,7,8,9,10]
n2 = 0
for i in range(len(num)):
    n2 += num[i]
print(n2)
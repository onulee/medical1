n1 = int(input('첫 번째 숫자를 입력해주세요:  '))
n2 = int(input('두 번째 숫자를 입력해주세요:  '))
sum1 = 0

# 1. n1 부터 n2까지의 합 
# (n1이 n2보다 클 경우 n1의 값이 무조건 n2 자리로 들어갈 수 있도록)

if n1 > n2:
    n1, n2 = n2, n1
for i in range(n1,n2+1):
    sum1 += i
print('{}부터 {}까지의 합은 {}입니다.'.format(n1,n2,sum1))


# 2. n1 부터 n2사이의 짝수, 홀수만의 합
sum2 = 0
if n1 > n2:
    n1, n2 = n2, n1
for i in range(n1,n2+1):
    if i % 2 == 0:
        sum1 += i
    else:
        sum2 += i
print('{}부터 {}사이의 짝수 값들의 합은 {}입니다.'.format(n1,n2,sum1))
print('{}부터 {}사이의 홀수 값들의 합은 {}입니다.'.format(n1,n2,sum2))

# 3. n1-n2까지의 홀수값을 저장
odd_list = []
for i in range(n1,n2+1):
    if i % 2 == 1:
        odd_list.append(i)
print(odd_list)

# 숫자 1개를 입력받아 1개를 출력하시오
# 1. 숫자 1개 입력
# 2. 숫자 1개 출력
num = int(input('숫자를 입력하세요:  ')) # str
num2 = int(input('숫자를 입력하세요:  '))
print(num)
print(num2)
print(num+num2)

# 숫자 5개를 입력받아 5개를 출력하세요
nums = []
for i in range(6):
    nums.append(int(input('숫자를 입력하세요:  ')))

print(nums)

# 5개의 합을 구해보세요
sum = 0
for i in range(6):
   sum += nums[i]

print('합계',sum)
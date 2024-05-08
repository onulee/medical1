import random
# 주택복권
# 2조711
# 1조740
# 1-9
# 0-999999

first_num = random.randint(1,9)
last_num = random.randint(0,999999)
lotto = str(first_num)+"조"+"{:06d}".format(last_num)
print(lotto)

l_input = input("복권을 입력하세요.(예:1조111)")
# 비교하는 프로그램을 구현하시오.
# 자리수를 활용하세요.
cnt = 0
for i in range(len(lotto)):
    if lotto[i] == l_input[i]:
        cnt += 1
    
print("맞는 개수 : ",cnt-1)        


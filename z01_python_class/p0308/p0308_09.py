import random
random_num = str(random.randint(10000,99999))
print("[ 랜덤숫자 맞추기 ]")
print("랜덤숫자 : ",random_num)
a_input = input("숫자 5자리를 입력하세요.")

# 숫자자리로 확인해서 맞춘 개수를 출력하시오.
# 12345 
# 35341
cnt = 0
# for i in range(len(str(random_num))):
for i in range(5):
    # i = 0,1,2,3,4
    if random_num[i]==a_input[i]:
        cnt += 1
    
print("맞는 개수 : ",cnt)
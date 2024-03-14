# 랜덤으로 숫자 1개 생성 1-100
# 입력한 숫자보다 크면 작은수를 입력하시오
# 입력한 숫자보다 작으면 큰수를 입력하시오.라고 멘트가 나오게
# 정답을 맞추면

# 총 입력한 횟수 : 7 회
# 현재까지 입력한 숫자 : 1,5,7,6,8,4,50

# 현재까지 입력했던 숫자를 모두 출력하시오.

import random

ran_num = random.randint(1,100)
in_num = 0
cnt = 1
s_list = []
while True:
    print("[ 랜덤숫자 맞추기 게임 ]")
    in_num = int(input(f"{cnt}번째 도전. 1-100까지의 숫자를 입력하세요.>> "))
    s_list.append(in_num)
    if ran_num > in_num:
        print("입력한 숫자보다 큰 수를 입력하세요.")
    elif ran_num < in_num:
        print("입력한 숫자보다 작은 수를 입력하세요.")    
    else:
        print("정답입니다.")
        break
    cnt += 1

#--- 종료 후 ---    
print("[ 결과 ]")
print(f"총 입력한 횟수 : {cnt} 회")
print(f"현재까지 입력한 숫자 : {s_list} 회")
  
    
    

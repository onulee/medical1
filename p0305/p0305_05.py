# 1-25까지 숫자를 랜덤으로 섞은 다음
# 2차원 리스트에 넣어보세요.
import random

num = random.randint(1,100)
cnt = 1 #도전횟수
save_num = []
print("정답:",num)
# 숫자맞추기 프로그램을 구현
# 1-10까지 숫자 랜덤으로 생성 숫자를 맞추는 프로그램입니다.
# 몇번째에 맞췄는지 출력하시오.
while True:
    in_num = int(input("1-100까지의 숫자를 입력하세요."))
    save_num.append(in_num) #저장
    if num>in_num:
        print("입력한 숫자보다 더 큽니다.")
    elif num<in_num:
        print("입력한 숫자보다 더 작습니다.")
    else:
        print("정답입니다.") 
        print("{}번째 도전을 하셨습니다.".format(cnt))
        break       
    cnt += 1

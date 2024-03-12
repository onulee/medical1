# 함수정의 : def 이름()
def machine(coffee):
    # 주문들어오면 진행
    print("1. 뜨거운 물을 준비한다.")
    print("2. 종이컵을 준비한다.")

    if coffee == 1:
        print("3. 보통커피를 탄다.")
    elif coffee == 2:
        print("3. 설탕커피를 탄다.")
    elif coffee == 3:
        print("3. 블랙커피를 탄다.")

    print("4. 물을 붓는다.")
    print("5. 스푼으로 젓는다.")
    print("손님에게 가져다 준다.")    
    print()
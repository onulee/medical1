import random 

# 화면출력함수
def screen():
    print("[ 로또번호 맞추기 프로그램 ]")
    print("1. 번호생성")
    print("2. 번호섞기")
    print("3. 나의 로또번호입력")
    print("4. 번호확인")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    return choice

# 번호생성함수
def num_generate(lotto):
    print("[ 번호생성 ]")
    # lotto = [ i for i in range(1,45+1)] #지역변수로 변환, 새롭게 재정의
    # print(lotto)
    for i in range(45):
        lotto[i] = i+1
    print(lotto) 

# 번호섞기함수    
def num_shuffle(lotto):
    print('[ 번호섞기 ]')
    random.shuffle(lotto)
    print(lotto) 
    
def num_input(my_lotto):
    print("[ 나의 로또번호입력 ]") 
    for i in range(6):
        my_num = int(input(f"{i+1}번째 로또번호를 입력하세요.>>"))
        my_lotto[i] = my_num
    print("내가 입력한 번호 : ",my_lotto)   

def num_check(lotto,lucky_lotto,my_lotto,win_num,win_amount):
    # win_num = [] # 지역변수로 인식이 되어서 주소값을 다시 세팅
    for i in range(6):
        lucky_lotto[i] = lotto[i]
    print("[ 번호 확인 ]") 
    print("로또번호 : ",lucky_lotto)
    print("내가 입력한 번호 : ",my_lotto) 
    # 몇개 맞췄는지 확인소스
    for i in my_lotto: # 1,20,21,23,25,44
        if i in lucky_lotto: #1,20,21,23,25,44
            win_num.append(i) # 
    print("당첨된 번호 : ",win_num)  #2개  
    # 당첨금액 출력  
    # print(f"당첨금액 : {win_amount[len(win_num)]} 원")
    print("* 당첨금액 : {:,d} 원".format(win_amount[len(win_num)]))
    print("-"*40)
    print()
import lotto        

#--------------------------------------------------
lotto = [0]*45       # 전체 45개 숫자
lucky_lotto = [0]*6 # [0,0,0,0,0,0] 당첨번호 6개 숫자  1,20,30,40,41,45
my_lotto = [0]*6    # 내가 입력한 6개 숫자 1,20,21,23,25,44
win_num = []     # 당첨된 번호 1,20
win_amount = [0,0,1000,10000,1000000,100000000,10000000000] #당첨금액

while True:
    choice = lotto.screen() # 화면출력함수 호출
    
    if choice == 1:
        lotto.num_generate(lotto)  # 번호생성함수 호출
            
    elif choice == 2:
        lotto.num_shuffle(lotto)   # 번호섞기함수 호출
    
    elif choice == 3:
        lotto.num_input(my_lotto)  # 나의 로또번호입력 
        
    elif choice == 4:
        lotto.num_check(lotto,lucky_lotto,my_lotto,win_num,win_amount)
        win_num = [] # 초기화
        
        
                   


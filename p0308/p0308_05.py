import random
# 리스트에 딕셔너리 형태로 변경
card_list = []
shape_list = ["spade","diamond","heart","clover"]
num_list = [0]*13
for i in range(1,14):
    num_list[i-1] = i
num_list[0] = "A"
num_list[10] = "J"
num_list[11] = "Q"
num_list[12] = "K"

# 카드 1세트를 구현 : 52장
card_list = [[0]*2 for i in range(52)]
cnt = 0
for i in shape_list: # "spade","diamond","heart","clover" 
    for j in range(13):
       card_list[cnt] = {"shape":i,"num":num_list[j]} 
       cnt += 1 

# 카드를 랜덤섞기
random.shuffle(card_list)

arr_num = 0
while True:
    print("[ 카드 게임 ]")
    print("-"*30)
    print("1. 카드1장 뽑기")
    print("2. 카드5장 뽑기")
    print("0. 종료")
    print("현재 남은 카드 : ",len(card_list) - arr_num) #len(card_list) - arr_num
    c_num = int(input("번호를 선택해주세요."))
    if c_num == 1:
        print("모양:{},번호:{}".format(card_list[arr_num]["shape"],card_list[arr_num]["num"]))
        arr_num += 1
    elif c_num == 2:
        for i in range(5):
            print("모양:{},번호:{}".format(card_list[arr_num]["shape"],card_list[arr_num]["num"]))
            print()
            arr_num += 1    
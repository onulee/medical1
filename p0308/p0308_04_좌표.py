import random
# 1. 0으로 25개 1차원 리스트 생성
aList = [0]*25

# 2. 1로 5개를 변경
for i in range(5):
    aList[i] = 1
    
# 3. 랜덤섞기
random.shuffle(aList)

# 4. 5*5 2차원 리스트에 넣기
checkList = [[0]*5 for i in range(5)] #5*5의 공간을 생성
for i in range(5):
    for j in range(5):
        checkList[i][j] = aList[5*i+j]  
       

# 추첨 5*5 2차원 배열
viewList = [["추첨"]*5 for i in range(5)] #5*5의 공간을 생성
c_count = 1       # 도전횟수
answer_count = 0  # 정답개수
my_xy = []        # 내가 입력한 좌표
while True:
    # 5. checkList 출력
    print("\t[ 5*5 checkList 좌표 ]")
    print("-"*40)
    print("",0,1,2,3,4,sep="\t")
    print("-"*40)
    for i in range(5):
        print(i,end="\t")
        for j in range(5):
            print(checkList[i][j],end="\t")
        print()    
    print("-"*40)

    # 6. viewList 출력
    print("\t[ 5*5 viewList 좌표 ]")
    print("-"*40)
    print("",0,1,2,3,4,sep="\t")
    print("-"*40)
    for i in range(5):
        print(i,end="\t")
        for j in range(5):
            print(viewList[i][j],end="\t")
        print()    
    print("-"*40)

    # 7. 좌표입력후 확인
    print("[ 현재 도전횟수 : {} 번 ]".format(c_count))
    x = int(input("가로 좌표를 입력하세요.>> "))
    y = int(input("세로 좌표를 입력하세요.>> "))
    if checkList[x][y] == 1:
        viewList[x][y] = "당첨"
        answer_count += 1
    else:
        viewList[x][y] = "[꽝]"
    
    # 내가 입력한 좌표 저장
    my_xy.append([x,y])   
    
    
    # 5개의 당첨을 맞추면 프로그램 종료
    if answer_count==5:
        print("[ 모두 정답 확인 ]")
        print("프로그램을 종료합니다.")
        break
    
    # 10번 시도후 프로그램 종료        
    c_count += 1    
    if c_count==10:
        print("[ 모두 도전 종료 ]")
        print("프로그램을 종료합니다.")
        break
    
print("[ 내가 입력한 좌표 출력 ]") 
print(my_xy)    
# 현재까지 입력한 좌표를 모두 출력하시오.

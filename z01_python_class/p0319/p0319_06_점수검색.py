stu = [
    ["홍길동",100],["유관순",98],["이순신",95],["김구",50],
    ["강감찬",99],["김유신",90],["홍길순",80],["홍길자",70]
]

while True:
    print("[ 학생성적 검색 ]")
    print("1. 이름으로 검색")
    print("2. 점수 검색")
    choice = int(input("원하는 번호를 입력하세요.>> "))
    
    if choice == 1:
        search = input("이름을 입력하세요.>> ")
        search_list = [] # 찾은 사람의 위치 저장
        cnt = 0
        # 검색어로 검색
        for s in stu:
            # if n.find(search) != -1:  # 검색어가 포함이 되어 있는지 확인
            if search in s[0]:  # 검색어가 포함이 되어 있는지 확인
                # print("찾는 사람이 있습니다. name리스트 위치 : ",cnt) 
                search_list.append(cnt)
            cnt += 1    

        # 검색된 사람들 출력
        if len(search_list) == 0:
            print("찾는 사람이 없습니다.")       
        else:
            print(f"{search} (으)로 검색된 사람 : ",end=" ")
            for i in search_list:
                print(stu[i][0],end=" ")  
            print()
            print()     
    
    elif choice == 2 :
        score = int(input("몇 점 이상을 검색하시겠습니까? "))
        # 80 -> 80점이상인 사람 이름이 출력되도록 해보세요.
        search_list = [] # 찾은 사람의 위치 저장
        cnt = 0
        # 검색어로 검색
        for s in stu:
            # if n.find(search) != -1:  # 검색어가 포함이 되어 있는지 확인
            if s[1] >= score:  # 검색어가 포함이 되어 있는지 확인
                # print("찾는 사람이 있습니다. name리스트 위치 : ",cnt) 
                search_list.append(cnt)
            cnt += 1    

        # 검색된 사람들 출력
        if len(search_list) == 0:
            print(f"{score} 보다 큰 점수는 없습니다.")       
        else:
            print(f"[ {score} 보다 큰 점수 ] ")
            for i in search_list:
                print(stu[i][0],":",stu[i][1])  
            print()
            print() 
    
    
    
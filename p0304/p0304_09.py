students = [[1,'홍길동',100,99,87,286,95.33,2],
            [2,'유관순',98,93,87,278,92.67,3],
            [3,'이순신',88,76,30,194,64.67,5],
            [4,'김구',100,100,100,300,100.00,1],
            [5,'강감찬',98,85,44,227,75.67,4]]

while True:
    # 강감찬
    search = input("삭제하려는 학생의 이름을 입력하세요.")
    
    # 이름찾기
    cnt = 0 # 찾은 학생의 위치
    # 전체학생 검색
    for stu in students:
        if stu[1]==search:
            break
        cnt += 1
    
    if cnt == len(students): #전체학생수
        print("{} 학생이 없습니다.".format(search))
    else:
        print("{} 학생을 찾았습니다.".format(search))
    
    print("찾은 위치 : ",cnt) 
    del students[cnt]
    print(students)       
    print("-"*40)        
students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}, 
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67}, 
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67}, 
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}, 
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
    ]


cnt = len(students)+1 #학번
while True:
    # 찾는 부분 프로그램 작성하시오.
    search = input("삭제하고자 하는 학생의 이름을 입력하세요.(0.취소)")
    chk = 0
    if search == "0":
        break
    for s_dic in students: #5명이 있으면 5번반복
        if s_dic["name"] == search:
            break
        chk += 1
    
    print("찾고자 하는 학생의 위치 :",chk)
    
        
    if chk >= len(students):
        print("찾고자 하는 학생이 없습니다.")
    else:
        print("{} 학생을 찾았습니다.".format(search))
        s_input = input("{} 학생 성적을 삭제하시겠습니까?(1.실행, 0.취소)".format(search))
        # 삭제
        if s_input != "1":
            print("삭제를 취소합니다.")
            break
        else:
            del students[chk]
            print("{} 학생성적이 삭제 되었습니다.".format(search))
            print(students)
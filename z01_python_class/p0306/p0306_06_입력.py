# students = [[S001,'홍길동',100,99,87,286,95.33,2],
#             [S002,'유관순',98,93,87,278,92.67,3],
#             [S003,'이순신',88,76,30,194,64.67,5],
#             [S004,'김구',100,100,100,300,100.00,1],
#             [S005,'강감찬',98,85,44,227,75.67,4]]

students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}, 
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67}, 
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67}, 
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}, 
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
    ]

cnt = len(students)+1 #학번
while True:
    name = input(f"{len(students)+1}번째 학생의 이름을 입력하세요.(0.취소)")
    if(name=="0"):
        print("학생 입력을 취소합니다.")
        break
    student= {} #데이터 초기화
    student["stuNo"] = "S"+"{:03d}".format(cnt)
    student["name"] = name  # 딕셔너리 추가
    kor = int(input("국어점수를 입력하세요."))
    student["kor"] = kor
    eng = int(input("영어점수를 입력하세요."))
    student["eng"] = eng
    math = int(input("수학점수를 입력하세요."))
    student["math"] = math
    total = kor+eng+math
    student["total"] = total
    avg = total/3
    student["avg"] = float("{:.2f}".format(avg))
    # list에 추가
    students.append(student)
    cnt += 1 #학번증가
    print("입력 데이터 :",student) #list -> dict
    print(students)



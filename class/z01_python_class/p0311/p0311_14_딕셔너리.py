# 함수선언
def stu_update(student): #지역변수 -> 주소값이 저장
    student["stuNo"] = 2
    student["name"] = "유관순"
    student["total"] = student["kor"]+student["eng"]+student["math"] #지역변수
    student["avg"] = student["total"]/3        #지역변수

# 프로그램 구현
student = {'stuNo': 1, 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 0, 'avg': 0} #2개의 이상의 변수


#함수호출
stu_update(student) #전역변수

print("학생1 : ",student) # 1,홍길동,100,100,100,300,100.0


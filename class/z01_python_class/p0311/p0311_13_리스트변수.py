# 함수선언
def stu_update(student): #지역변수 -> 주소값이 저장
    student[0] = 2
    student[1] = "유관순"
    student[5] = student[2]+student[3]+student[4] #지역변수
    student[6] = student[5]/3        #지역변수

# 프로그램 구현
student = [1,"홍길동",100,100,100,0,0] #2개의 이상의 변수


#함수호출
stu_update(student) #전역변수

print("학생1 : ",student) # 1,홍길동,100,100,100,300,100.0


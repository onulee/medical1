# 함수선언
def stu_update(stuNo,name,kor,eng,math): #지역변수
    stuNo = 2
    name = "유관순"
    total = kor+eng+math #지역변수
    avg = total/3        #지역변수
    return stuNo,name,total,avg

# 프로그램 구현
stuNo = 1
name = "홍길동"
kor = 100
eng = 100
math = 100
total = 0
avg = 0

#함수호출
stuNo,name,total,avg = stu_update(stuNo,name,kor,eng,math) #전역변수

print("학생1 : ",stuNo,name,kor,eng,math,total,avg) # 1,홍길동,100,100,100,300,100.0


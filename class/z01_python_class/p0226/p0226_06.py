
student = []

# 두 명 이상의 학생의
# 이름, 국,영,수 점수를 입력받아
stu_name1 = input("1. 이름을 입력해주세요:  ")
kor = int(input("국어 점수:  "))
eng = int(input("영어 점수:  "))
math = int(input("수학 점수:  "))
total = kor+eng+math
avg = total/3
stu1 = [stu_name1,kor,eng,math,total,avg]

stu_name2 = input("2. 이름을 입력해주세요:  ")
kor = int(input("국어 점수:  "))
eng = int(input("영어 점수:  "))
math = int(input("수학 점수:  "))
total = kor+eng+math
avg = total/3
stu2 = [stu_name2,kor,eng,math,total,avg]
# 리스트를 생성한 후
# student 리스트에 넣어주세요
student.append(stu1)
student.append(stu2)
# student 리스트 전체 출력
print(student)
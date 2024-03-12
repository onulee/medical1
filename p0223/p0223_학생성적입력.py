# 학생 성적 입력

# 변수를 사용합니다.
stu_name = input("학생 이름을 입력해주세요:  ")
kor = int(input("국어 성적 입력:  "))
eng = int(input("영어 성적 입력  "))
math = int(input("수학 성적 입력:  "))
total = kor+eng+math
avg = total/3

print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(1,stu_name,kor,eng,math,total,avg,1))

stu = [1, '홍길동', 100, 100, 100, 300, 100.0, 1]
stu1 = [1, stu_name, kor, eng, math, total, avg, 1]

print(stu)
print(stu1)

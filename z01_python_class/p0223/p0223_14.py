# 리스트를 사용해서 출력
stu1 = [1, '홍길동',100,100,100,300,100.0,1]
stu2 = [2, '유관순', 90,90,90,270,90.0,2]

print("[ 학생 성적 출력 ]")
print('-'*18)
print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(stu1[0],stu1[1],stu1[2],stu1[3],stu1[4],stu1[5],stu1[6],stu1[7]))  # 홍길동
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(stu2[0],stu2[1],stu2[2],stu2[3],stu2[4],stu2[5],stu2[6],stu2[7]))  # 유관순
print('-'*62)


# 기존 변수를 사용해서 출력
stu_no1 = 1
stu_name1 = '홍길동'
kor1 = 100
eng1 = 100
math1 = 100
total1 = kor1+eng1+math1
avg1 = total1/3
rank1 = 0

print("[ 학생 성적 출력 ]")
print('-'*18)
print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(stu_no1,stu_name1,kor1,eng1,math1,total1,avg1,rank1))
print('-'*62)
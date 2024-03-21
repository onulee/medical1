# print('{}\t{}\t{} \t{} \t{}  \t{}  \t{}  \t{}'.format(
#     1,'홍길동',100,100,100,300,100.0,1
# ))

# 입력
stu_name1 = input('첫번째 학생이름을 입력하세요 >>')
kor1 = int(input('첫번째 학생의 국어점수를 입력하세요 >> '))
eng1 = int(input('첫번째 학생의 영어점수를 입력하세요 >> '))
math1 = int(input('첫번째 학생의 수학점수를 입력하세요 >> '))
total1 = kor1+eng1+math1
avg1 = total1/3

stu_name2 = input('두번째 학생이름을 입력하세요 >>')
kor2 = int(input('두번째 학생의 국어점수를 입력하세요 >> '))
eng2 = int(input('두번째 학생의 영어점수를 입력하세요 >> '))
math2 = int(input('두번째 학생의 수학점수를 입력하세요 >> '))
total2 = kor2+eng2+math2
avg2 = total2/3

# 출력
print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t{}\t{} \t{} \t{}  \t{}  \t{:.2f}  \t{}'.format(
    1,stu_name1,kor1,eng1,math1,total1,avg1,1
))
print('{}\t{}\t{} \t{} \t{}  \t{}  \t{:.2f}  \t{}'.format(
    1,stu_name2,kor2,eng2,math2,total2,avg2,1
))

# stu_no1, stu_no2, stu_name1, stu_name2, kor1, kor2
# eng1, eng2, math1, math2, total1, total2, avg1, avg2
# stu_name1 = input('첫번째 학생이름을 입력하세요 >>')
# stu_name2 = input('두번째 학생이름을 입력하세요 >>')

# 홍길동 100 100 100
# 유관순 90  100 90 
# 두 정보를 입력을 받아서 출력해보세요 
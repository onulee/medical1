# 2명의 학생의 이름, 국어, 영어, 수학 점수를 입력받아
# 합계를 출력하시오

students = []

for i in range(3):
    student = []  # 초기화
    student.append(input('이름을 입력하세요:  '))
    student.append(int(input('국어 성적 입력:  ')))
    student.append(int(input('영어 성적 입력:  ')))
    student.append(int(input('수학 성적 입력:  ')))
    sum = student[1]+student[2]+student[3]  # student[0] =  이름
    student.append(sum)
    student.append('{:.2f}'.format(sum/3))
    students.append(student)

# 합계
print(student)
# 전체학생출력
print('[ 학생성적 출력 ]')
print('-'*50)
print('이름\t국어\t영어\t수학\t합계\t평균')
print('-'*50)

# 2차원 리스트는 for문을 2번 사용함
for stu in students:
    for s in stu:
        print(s, end ='\t')
    print()

# 3명의 국어점수 합계, 평균을 출력하시오.
kors,engs,maths,totals = 0,0,0,0 
for j, stu in enumerate(students):
    kors += stu[1]
    engs += stu[2]
    maths += stu[3]
    totals += stu[4]
avgs = totals / len(students)
print()
print('합계\t{}\t{}\t{}\t{}\t{}'.format(kors,engs,maths,totals,avgs))
print()
# 학생 이름, 국어, 영어, 수학 점수를 입력받아서 
# 아래와 같이 출력을하고
# 입력
stu_name1 = input('첫번째 학생이름을 입력하세요 >>')
kor1 = int(input('첫번째 학생의 국어점수를 입력하세요 >> '))
eng1 = int(input('첫번째 학생의 영어점수를 입력하세요 >> '))
math1 = int(input('첫번째 학생의 수학점수를 입력하세요 >> '))
total1 = kor1+eng1+math1
avg1 = total1/3

# 출력
print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t{}\t{} \t{} \t{}  \t{}  \t{:.2f}  \t{}'.format(
    1,stu_name1,kor1,eng1,math1,total1,avg1,1
))
# 만약에 평균이 80점이상이면 합격입니다를 출력하세요 
# if(조건문)사용
if avg1 >= 80:
    print('{}님 합격입니다'.format(stu_name1))
else:
    print('{}님 불합격입니다'.format(stu_name1))
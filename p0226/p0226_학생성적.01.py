
student = [[1,'홍길동',100,100,100,300,100.0,1],\
    [2, '유관순',90,90,90,270,90.0,2]]
print(student)

print('-'* 35)
print('\t[ 학생성적 프로그램 ]')
print('1. 학생성적입력')
print('4. 학생성적전체출력')
print('-'*35)
ch = input('원하는 번호를 입력하세요:  ')

if ch == '1':
    print('[ 학생성적입력 ]을 선택하셨습니다.')
    print('-'*40)
    print('[ 학생성적입력 ]')
    print('-'*40)
    no = int(input('> 번호 입력:  '))
    name = input("> 학생 이름 입력:  ")
    kor = int(input("> 국어 성적:  "))
    eng = int(input('> 영어 성적:  '))
    math = int(input('> 수학 성적:  '))
    total = kor+eng+math
    avg = total/3
    rank = int(input('등수 입력:  '))
    stu1 = [no,name,kor,eng,math,total,avg,rank]
    print(stu1)
elif ch == '4':
    print('[ 학생성적전체출력 ]을 선택하셨습니다.')
    print('-'*40)
    print('[ 학생성적전체출력 ]')
    print('-'*40)
    name1 = input("> 학생 이름:   ")
    if name1 == "홍길동":
        print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(student[0][0],student[0][1],student[0][2],student[0][3],student[0][4],student[0][5],student[0][6],student[0][7]))
        print('-'*65)
    elif name1 == '유관순':
        print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(student[1][0],student[1][1],student[1][2],student[1][3],student[1][4],student[1][5],student[1][6],student[1][7]))
        print('-'*65)
    else:
        print(">> 조회된 기록이 없습니다. 다시 한번 입력해주세요. <<")
        print('-'*65)
else:
    print(">> 선택된 서비스가 없습니다. 다시 한 번 입력해주세요. <<")
    print('-'*50)
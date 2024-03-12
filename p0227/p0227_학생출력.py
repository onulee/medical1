
student= []
for i in range(5):
    print('-'*35)
    print('\t[ 학생성적프로그램 ]')
    print('1. 학생성적입력')
    print('4. 학생성적전체출력')
    print('0. 프로그램 종료')
    print('-'*35)
    print('[',str(i+1),']번째 창:' )
    ch = input('원하시는 서비스 번호를 입력하세요:  ')
    
    if ch == '1': # if 문을 사용해서 1을 누르면 [학생성적입력]
        print('[ 학생성적입력 ]')
        print('-'*35)
        name = input('이름:  ')
        kor = int(input('국어 성적:  '))
        eng = int(input('영어 성적:  '))
        math = int(input('수학 성적:  '))
        total = kor+eng+math
        avg = total/3
        stu = [name,kor,eng,math,total,avg]
        student.append(stu)
    elif ch == '4':        # 4를 누르면 [학생성적전체출력]
        print('[ 학생성적전체출력 ]')
        print('-'*35)
        print('이름\t국어\t영어\t수학\t총점\t평균')
        for i in range(len(student)):
            print('{}\t{}\t{}\t{}\t{}\t{}'.format(student[i][0],student[i][1],student[i][2],student[i][3],student[i][4],student[i][5]))
    elif ch == '0':        # 0을 누르면 [프로그램 종료]
        print('[ 프로그램 종료 ]')
    else:
        print('선택된 서비스가 없습니다. 다시 입력해주세요.')
    
    print('*'*35)
    
print('------------ 프로그램이 종료되었습니다. ------------')
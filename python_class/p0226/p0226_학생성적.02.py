
# for를 사용해서 5번 반복
student= []

for i in range(5):
    print('-'*35)
    print('\t[ 학생성적프로그램 ]')
    print('1. 학생성적입력')
    print('4. 학생성적전체출력')
    print('0. 프로그램 종료')
    print('-'*35)
    ch = input('원하는 번호를 입력하세요:  ')
    
    if ch == '1': # if 문을 사용해서 1을 누르면 [학생성적입력]
        print('[ 학생성적입력 ]')
        print('-'*35)
        name = input('이름:  ')
        kor = int(input('국어 성적:  '))
        eng = int(input('영어 성적:  '))
        math = int(input('수학 성적:  '))
        stu1 = [name,kor,eng,math]
        student.append(stu1)
    elif ch == '4': # 4를 누르면 [학생성적전체출력]
        print('[ 학생성적전체출력 ]')
        print('-'*35)
        print('이름\t국어\t영어\t수학')
        for i in range(0,len(student)):
            print('{}\t{}\t{}\t{}'.format(student[i][0],student[i][1],student[i][2],student[i][3]))
    elif ch == '0': # 0을 누르면 [프로그램 종료]
        print('[ 프로그램 종료 ]')
    else:
        print('선택된 서비스가 없습니다. 다시 입력해주세요.')
    
    print('*'*35)


    

# 학생정보수정
students = [[1,'홍길동',100,100,99,299,99,97],\
    [2,'유관순',100,100,99,299,99,99.97],
    [3,'이순신',100,100,99,299,99,99,97]]

while True:
    search = input('찾는 학생의 이름을 입력하세요(0.취소):  ')
    if search == '0':
        break
    chk = 0
    count = 0
    for stu in students:
        if search in stu:
            chk = 1
            break
        count += 1 # 찾는 학생의 위치값
    if chk == 0:
        print('찾는 학생의 정보가 없습니다.')
    else:
        print('{}학생의 정보를 찾았습니다.'.format(search))
        num = input('1. 국어 2. 영어 3. 수학 중 원하시는 과목 수정 번호를 입력하세요:  ')
        if num == '1' or num == '국어':
            print('국어성적 수정을 선택하셨습니다.')
            print('-'*50)
            # 성적 수정 프로그램 구현
            print('{}님의 국어 성적은 {}점 입니다.'.format(search,students[count][2]))
            re_kor = int(input('국어 성적 수정값 입력:  '))
            students[count][2] = re_kor
            print('{}님의 수정된 국어 성적: {}'.format(search,re_kor))
        elif num == '2' or num == '영어':
            print('영어성적 수정을 선택하셨습니다.')
            print('-'*50)
            print('{}님의 영어 성적은 {}점 입니다.'.format(search,students[count][3]))
            re_eng = int(input('영어 성적 수정값 입력:  '))
            students[count][3] = re_eng
            print('{}님의 수정된 국어 성적: {}'.format(search,re_eng))
        elif num == '3' or num == '수학':
            print('수학성적 수정 선택하셨습니다.')
            print('-'*50)
            print('{}님의 수학 성적은 {}점 입니다.'.format(search,students[count][4]))
            re_math = int(input('수학 성적 수정값 입력:  '))
            students[count][4] = re_math
            print('{}님의 수정된 수학 성적: {}'.format(search,re_math))
        else:
            print('잘못입력하셨습니다. 다시 입력해주세요')
    students[count][5] = students[count][2]+students[count][3]+students[count][4]
    students[count][6] = students[count][5] / 3
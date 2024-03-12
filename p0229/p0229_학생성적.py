students = []
cnt = 0
count = 0
while True:
    cnt += 1
    print('[',cnt,']번째 창:' )
    print('-'*35)
    print('\t'+'[ 학생성적프로그램 ]')
    print('1. 학생성적입력')
    print('2. 학생성적수정')
    print('3. 학생성적삭제')
    print('4. 학생성적전체출력')
    print('5. 학생검색출력')
    print('6. 등수처리')
    print('0. 프로그램 종료')
    print('-'*35)
    ch = input('원하시는 서비스 번호를 입력하세요:  ')
    
    if ch.isdigit():
        ch = int(ch)
    print('-'*40)
    if ch == 1:
        print('** 학생성적입력')
        stu_name = input('이름을 입력하세요:  ')
        kor = int(input('국어 성적 입력:  '))
        eng = int(input('영어 성적 입렵:  '))
        math = int(input('수학 성적 입력:  '))
        total = kor+eng+math
        avg = total / 3
        count += 1
        stu = [count, stu_name, kor, eng, math, total, avg]
        students.append(stu)
    elif ch == 2:
        print('** 학생성적수정')
        rename = input('성적수정을 원하는 학생의 이름을 입력하세요:  ')
        for i, n in enumerate(students):
            if rename in n:  # 존재한다면
                print(rename,'님을 선택하셨습니다.')
                ch_score = input('수정하고 싶은 과목을 고르세요 (1. 국어, 2. 영어, 3.수학):  ')
                print('-'*40)
                if ch_score.isdigit():
                    ch_score = int(ch_score)
                if ch_score == 1:
                    print('국어 성적 수정을 선택하셨습니다.')
                    print('-'*40)
                    print(rename,'님의 국어성적은',students[i][2],'점 입니다.')
                    re_kor = int(input('몇 점으로 수정할까요?:  '))
                    students[i][2] = re_kor
                elif ch_score == 2:
                    print('영어 성적 수정을 선택하셨습니다.')
                    print('-'*40)
                    print(rename,'님의 영어성적은',students[i][3],'점 입니다.')
                    re_eng = int(input('몇 점으로 수정할까요?:  '))
                    students[i][3] = re_eng
                elif ch_score == 3:
                    print('수학 성적 수정을 선택하셨습니다.')
                    print('-'*40)
                    print(rename,'님의 수학성적은',students[i][4],'점 입니다.')
                    re_math = int(input('몇 점으로 수정할까요?:  '))
                    students[i][4] = re_math
                else:
                    print('잘못 입력하셨습니다.')
            else:
                print('해당 학생은 리스트에 없습니다.')
    elif ch == 3:
        print('** 성적삭제')
        print('-'*40)
        delName = input('성적을 삭제할 학생의 이름을 입력하세요:  ')
        for i, delete in enumerate(students):
            if delName in delete: # 존재한다면
                del(students[i])
        print('{}님의 성적이 삭제되었습니다.'.format(delName))
        print('-'*40)
    elif ch == 4:
        print('** 학생성적전체출력')
        print('번호\t이름\t국어\t영어\t수학\t총점\t평균')
        for i in range(len(students)):
            print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}'.format(students[i][0],students[i][1],\
                students[i][2],students[i][3],students[i][4],students[i][5],students[i][6]))
        print('-'*40)
    elif ch == 5:
        print('** 학생검색출력')
        print('-'*40)
        searName = input('검색할 학생의 이름을 입력하세요:  ')
        print('번호\t이름\t국어\t영어\t수학\t총점\t평균')
        for i, search in enumerate(students):
            if searName in search:
                print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}'.format(search[0],search[1],search[2],\
                    search[3],search[4],search[5],search[6]))
            else:
                print('조회된 학생 성적이 없습니다.')
        print('-'*40)
    elif ch == 6:
        pass
    elif ch == 0:
        print('프로그램을 종료합니다.')
        print('*'*40)
        break
    else:
        print('해당하는 서비스가 없습니다. 다시 입력하세요')
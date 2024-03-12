# students = []
students = [[1,'홍길동',100,99,87,286,95.33,2],
            [2,'유관순',98,93,87,278,92.67,3],
            [3,'이순신',88,76,30,194,64.67,5],
            [4,'김구',100,100,100,300,100.00,1],
            [5,'강감찬',98,85,44,227,75.67,4]]
student = [] # 학생성적저장
cnt = len(students)
# 학생번호 사용
while True:
    print('-'*40)
    print('[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램 종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요:  ')
    print('-'*40)
    if not choice.isdigit():
        print('숫자만 입력 가능합니다.')
        continue # 반복문 계속실행
    choice = int(choice)
    
    # 1. 학생성적입력 프로그램
    if choice == 1 :
        while True :
            print('학생성적을 입력합니다.')
            student = []  # 초기화
            cnt += 1
            student.append(cnt)
            name = input('이름을 입력하세요:  (0. 취소)  ')
            student.append(name)
            if name == "0":
                break
            kor = int(input('국어 성적 입력:  '))
            eng = int(input('영어 성적 입력:  '))
            math = int(input('수학 성적 입력:  '))
            total = kor+eng+math
            avg = total / 3
            student = [cnt,name,kor,eng,math,total]
            # 합계 저장
            # 평균 저장
            student.append('{:.2f}'.format(avg))
            student.append(1)
            students.append(student)

    # 2. 학생성적전체출력 프로그램
    elif choice == 2 :
        print('[ 학생성적전체출력 ]')
        print('-'*55)
        print('학번\t이름\t국어\t영어\t수학\t합계\t평균')
        print('-'*55)
        for stu in students:
            for s in stu:
                print(s,end ='\t')
            print()
        kors,engs,maths,totals = 0,0,0,0 
        for j, stu in enumerate(students):
            kors += stu[2]
            engs += stu[3]
            maths += stu[4]
            totals += stu[5]
        avgs = totals / len(students)
        print()
        print('--\t합계\t{}\t{}\t{}\t{}\t{:.2f}'.format(kors,engs,maths,totals,avgs))
        print()
    
    elif choice == 3 :
        while True:
            search = input('검색하고 싶은 학생 이름을 입력하세요(0.취소):  ')
            chk = 0  # 찾는 정보 확인
            count = 0
            if search == '0':
                break
            for stu in students: # 홍길동, 유관순, 이순신
                if search in stu:
                    chk = 1 # 정보를 찾았을 때 정보를 1로 변경
                    break
                count += 1
            if chk == 1:
                print('{}의 학생정보를 찾았습니다.'.format(search))
                # 전체학생 정보출력
                print('[ {} 학생성적 출력 ]'.format(search))
                print('-'*50)
                print('학번\t이름\t국어\t영어\t수학\t합계\t평균')
                print('-'*50)
                for i in students[count]:
                    print(i,end= "\t")
                print()
            else:
                print('찾는 학생의 정보가 없습니다.')
    elif choice == 4:
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
                    print('{}님의 수정된 국어 성적: {}점'.format(search,re_kor))
                elif num == '2' or num == '영어':
                    print('영어성적 수정을 선택하셨습니다.')
                    print('-'*50)
                    print('{}님의 영어 성적은 {}점 입니다.'.format(search,students[count][3]))
                    re_eng = int(input('영어 성적 수정값 입력:  '))
                    students[count][3] = re_eng
                    print('{}님의 수정된 국어 성적: {}점'.format(search,re_eng))
                elif num == '3' or num == '수학':
                    print('수학성적 수정 선택하셨습니다.')
                    print('-'*50)
                    print('{}님의 수학 성적은 {}점 입니다.'.format(search,students[count][4]))
                    re_math = int(input('수학 성적 수정값 입력:  '))
                    students[count][4] = re_math
                    print('{}님의 수정된 수학 성적: {}점'.format(search,re_math))
                else:
                    print('잘못입력하셨습니다. 다시 입력해주세요')
            students[count][5] = students[count][2]+students[count][3]+students[count][4]
            students[count][6] = '{:.2f}'.format(students[count][5]/3)
    elif choice == 5:
        while True: 
            ch = input('등수처리를 실행하시겠습니까? (1.실행 0.취소):  ')
            if ch == '0':
                print('등수처리를 취소하였습니다.')
                break
            elif ch == '1':
                print('[ 등수처리 ]')
                print('-'*40)
                for i, i_stu in enumerate(students):
                    no = 1 # 초기화
                    for j, j_stu in enumerate(students):
                        if i_stu[5] < j_stu[5]:
                            no += 1 # 비교대상 총합이 더 크면 1 증가
                    i_stu[7] = no # 등수 위치에 no 저장
            else:
                print('잘못입력하셨습니다. 다시 입력해주세요.')
            print('등수처리가 완료되었습니다.')
            print('-'*40)
    # 학생삭제          
    elif choice == 6:
        while True:
            search = input("삭제하려는 학생의 이름을 입력하세요.")
            
            # 이름찾기
            cnt = 0 # 찾은 학생의 위치
            # 전체학생 검색
            for stu in students:
                if stu[1]==search:
                    break
                cnt += 1
            
            if cnt == len(students): #전체학생수
                print("{} 학생이 없습니다.".format(search))
            else:
                choice = input("{} 학생을 찾았습니다.삭제하시겠습니까?(1.삭제 0.취소)".format(search))
                if choice == "1":
                    print("{}학생의 데이터가 삭제되었습니다.".format(search))
                    del students[cnt]
                else:
                    print("삭제가 취소되었습니다.")    
            
            print(students)  
            
    elif choice == 0:
        print('프로그램을 종료합니다.')
        break  # 반복문 종료
    else:
        print('선택된 서비스가 없습니다.')
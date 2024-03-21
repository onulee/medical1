students = [[1,'홍길동',100,100,99,299,99.97,1],
    [2,'유관순',100,100,99,299,99.97,1],
    [3,'이순신',100,100,99,299,99.97,1],
    [4, '김구',100,100,90,290,96.67,1],
    [5,'김유신',90,70,50,210,70.0,1]]

# 등수처리

while True: 
    choice = input('등수처리를 실행하시겠습니까? (1.실행 0.취소):  ')
    if choice == '0':
        print('등수처리를 취소하였습니다.')
        break
    elif choice == '1':
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
    print(students)
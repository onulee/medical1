
member= []
# 이름만 입력 받아서 [1. 홍길동],[2. 유관순],[3. 이순신]의 배열로 출력하기
count = 0
cnt = 0
while True:
    cnt += 1
    print('[ {}번째 물음 ]'.format(cnt))
    print('1. 입력')
    print('2. 출력')
    print('3. 검색')
    print('4. 검색 후 삭제')
    print('5. 정보 수정')
    print('0. 종료')
    ch = input('원하는 서비스의 번호를 입력하세요:  ')
    if ch.isdigit():
        ch = int(ch)
    print('-'*40)
    if ch == 1:
        print('** 입력')
        name = input('이름을 입력하세요:  ')
        count += 1
        m = [count, name]
        member.append(m)
    elif ch == 2:
        print('** 출력')
        print('번호\t이름')
        for i in range(len(member)):
            print('{}\t{}'.format(member[i][0],member[i][1]))
        print('-'*40)
    elif ch == 3:
        print('** 검색')
        searName = input('검색할 학생의 이름을 입력하세요:  ')
        print('번호\t이름')
        for i, m in enumerate(member):
            if searName in m: # 존재한다면
                print('{}\t{}'.format(m[0],searName))
            else:
                print('{}\t{}'.format('.','.'))
        print('-'*40)
    elif ch == 4:
        print('** 검색 후 삭제')
        delName = input('삭제할 학생의 이름을 입력하세요:  ')
        for i, stu in enumerate(member):
            if delName in stu: # 존재한다면
                del(member[i])
        print('{}님이 삭제되었습니다.'.format(delName))
        print('-'*40)
    elif ch == 5:
        print('** 정보 수정')
        reName = input('수정하고 싶은 학생의 이름을 입력하세요:  ')
        for i, n in enumerate(member):
            if reName in n: # 존재한다면
                print(reName, '님을 선택하셨습니다.')
                ch_num = int(input('수정하고 싶은 항목을 선택해주세요 (1. 번호수정, 2. 이름수정):  '))
                print('-'*40)
                if ch_num == 1:
                    print(reName,'님의 번호 수정을 선택하셨습니다.')
                    print('-'*40)
                    print(reName,'님의 번호는', member[i][0],'입니다.')
                    reNum = int(input('>> 무슨 번호로 수정할까요?:  '))
                    member[i][0] = reNum
                elif ch_num == 2:
                    print(reName,'님의 이름 수정을 선택하셨습니다.')
                    print(reName,'님의 이름은', member[i][1],'입니다.')
                    stu_name = input('>> 변경할 이름을 입력해주세요:  ')
                    member[i][1] = stu_name
                else:
                    print('잘못 입력하셨습니다.')
            else:
                print('해당 학생은 리스트에 없습니다.')
    elif ch == 0:
        print('프로그램을 종료합니다.')
        print('*'*40)
        break
    else:
        print('다시 입력하세요')
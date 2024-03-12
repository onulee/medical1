print('-'*35)
print('[ 학생성적프로그램 ]')
print('-'*35)
print('1. 학생성적입력')
print('2. 학생성적수정')
print('3. 학생성적삭제')
print('4. 학생성적전체출력')
print('5. 학생성적검색출력')
print('6. 등수처리')
print('0. 프로그램 종료')
print('-'*35)
choice = int(input('원하는 번호를 입력하세요:  '))

# 만약에 1을 입력하면 [학생성적입력을 선택하였습니다.] 출력할 수 있도록

if choice == 1:
    print('[ 학생성적입력 ]을 선택하셨습니다.')
elif choice == 2:
    print('[ 학생성적수정 ]을 선택하셨습니다.')
elif choice == 3:
    print('[ 학생성적삭제 ]를 선택하셨습니다.')
elif choice == 4:
    print('[ 학생성적전체출력 ]을 선택하셨습니다.')
elif choice == 5:
    print('[ 학생성적검색출력 ]을 선택하셨습니다.')
elif choice == 6:
    print('[ 등수처리 ]를 선택하셨습니다.')
elif choice == 0:
    print('[ 프로그램 종료 ]')
else:
    print("잘못 입력하셨습니다. 다시 입력해주세요.")
print('-'*35)
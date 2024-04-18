member = []

# 입력 : 이름, 점수 (input)
# 총 3명의 정보를  member 리스트에 넣으세요

# for i in range(3):
#     print('*',str(i+1),'번째 입력')
#     name = input("이름:  ")
#     score = int(input("점수 입력:  "))
#     stu = [name,score]
#     member.append(stu)
# print(member)

member = [['이순신', 90], ['홍길동', 100], ['유관순', 95]]
for i in range(0,len(member)):
    if member[i][1] >= 60:
        print('{}님 {}점으로 합격입니다.'.format(member[i][0],member[i][1]))
    else:
        print('{}님 {}점으로 불합격입니다.'.format(member[i][0],member[i][1]))
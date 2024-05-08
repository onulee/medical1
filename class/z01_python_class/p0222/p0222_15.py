import datetime # 날짜 관련 기능을 가져옴 
now = datetime.datetime.now() # 오늘 날짜 시분초 가져옴
year = now.year # 2024

# 현재는 [17]시 입니다. 
# 시간을 사용해서 
# 지금이 오전이면 오전입니다. 오후면 오후입니다 출력
h = now.hour # 시간 
# 오전
if h < 12 :
    print('현재는 {}시로 오전입니다.'.format(h))
else:
    print('현재는 {}시로 오후입니다.'.format(h))
# [현재는 17시로 오후입니다.] 

m = now.month
print(type(m)) # type을 알아보는 방법: <class 'int'>
# 1.짝수달입니다. 홀수달 입니다 
# now.month => 2 [짝수달입니다]
if m % 2 == 0:
    print('짝수달 입니다.')
else:
    print('홀수달 입니다.')
# 2. 월 겨울 3-11월이면 겨울이 아닙니다. 그 외의 경우에는 겨울입니다 
# 겨울입니다. 겨울이 아닙니다. 
if 3 <= m <= 11:
    print('겨울이 아닙니다')
else:
    print('겨울입니다')




# print(now) # => 2024-02-22 17:06:53.323195
# print(now.year) # 연도
# print(now.month) # 월
# print(now.day) # 일
# print(now.hour)
# print(now.minute)
# print(now.second)
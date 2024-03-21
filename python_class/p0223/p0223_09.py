import datetime

now = datetime.datetime.now()  # 현재를 가져옴
print(now)
# 2024-02-23 13:03:09.195335

month = now.month # 현재 월
# 현재가 봄 여름 가을 겨울
# 12,1,2 겨울, 3,4,5 봄 6,7,8 여름 9,10,11 가을
# elif 를 사용하여 출력

if 3 <= month <= 5:
    print("현재 계절은 봄 입니다.")
elif 6 <= month <= 8:
    print("현재 계절은 여름 입니다.")
elif 9 <= month <= 11:
    print("현재 계절은 가을 입니다.")
else:
    print("현재 계절은 겨울 입니다.")
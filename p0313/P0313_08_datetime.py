# from datetime import datetime
import datetime
# print(datetime.now(timezone('Asia/Seoul')))

now = datetime.datetime.now()
print("시간을 포맷에 맞춰 출력하기")
# Y 년을 의미, m:월 d:일 H:시 M:분 S:초
# 일자시간의 포맷을 설정하는 함수
output_a = now.strftime("%Y년 %m월 %d일 %H시 %M분 %S초")
output_b = now.strftime("%Y-%m-%d %H:%M:%S")
output_c = now.strftime("%Y/%m/%d %H:%M:%S")
output_d = now.strftime("%Y/%m/%d")

print(output_a)
print(output_b)
print(output_c)
print(output_d)

# import datetime
# # from datetime import datetime

# print("현재시각 출력")
# now = datetime.datetime.now()

print(now.year+1,"년")
print(now.month,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second, "초")
print()
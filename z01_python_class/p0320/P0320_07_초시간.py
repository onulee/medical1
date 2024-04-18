from datetime import datetime
import time

# strftime : 특정한 형태로 출력
for i in range(10):
    now = datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(1)


# # a = 123
# # print(a[0])

# # 자리배열은 문자열만 가능, 숫자는 불가능
# b="123"
# print(b[0])
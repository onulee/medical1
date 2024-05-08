# split() #문자열 분리

hobby = "게임,골프,독서"

# 리스트타입 3개로 분리
print(hobby.split(","))

h_data = "2023-10-23,1,강원도 강릉시,강릉동인병원,383,21,033)651-6167,강릉대로419번길 42,종합"
h_list = h_data.split(",")
print("병상수 : ",h_list[4])

a_data="2023-10-23/1/강원도 강릉시/강릉동인병원/383/21/033)651-6167/강릉대로419번길 42/종합"
a_list = a_data.split("/")
print("병상수 : ",a_list[4])

ss = "%"
print(ss.join('파이썬'))

s_date = "2023/03/08"
s_date_list = s_date.split("/")
print(s_date_list)

s_time = "2023:03:08:16:48:00"
#리스트로 분리해서 출력하시오.
s_time_list = s_time.split(":")
print(s_time_list)

today = "2024/03/08"
# 10년후의 날짜를 출력하시오. 2034/03/08
today_list = today.split("/")
today_list[0] = int(today_list[0])+10
# today2 = "{}/{}/{}".format(today_list[0],today_list[1],today_list[2])
today2 = "{}/{}/{}".format(*today_list)
print(today2)






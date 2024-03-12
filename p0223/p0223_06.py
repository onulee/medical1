# if - else
# if - elif - else
'''
if 조건문1 :
    실행문1
elif 조건문2:
    실행문2
else:
    실행문3
    
조건문1이 참이면 실행문1 실행 후 종료
조건문1이 거짓이고 조건문2가 참이면 실행문2 실행 후 종료
조건문1, 조건문2가 거짓이면 실행문3 실행 후 종료
'''

weather = '눈'
if weather == '비':
    print('비가 오네요 우산을 챙겨주세요')
elif weather == '눈':
    print('눈이옵니다. 조심하세요')
else:
    print('선크림을 발라주세요')
    

# 변수가 양수이면 양수, 음수이면 음수 0이면 0이라고 출력해보세요!
num = float(input("숫자 하나를 입력해주세요:  ")) # int를 넣어도 됨
if num > 0 :
    print("[ 양수입니다.]")
elif num < 0:
    print('[ 음수입니다.]')
elif num == 0:           # else: print('0') 도 가능
    print("[ 0 입니다.]")


# 돈이 만원이상 [택시를 탄다] 2천원 이상 [버스를 탄다]
# 천원 이상 [따릉이를 탄다] 나머지 [걸어간다]

money = int(input("현재 가지고 있는 돈:  "))

if money >=10000:
    print("[ 택시를 타고 간다.]")
elif money >= 2000:
    print("[ 버스를 타고 간다.]")
elif money >= 1000:
    print('[ 따릉이를 타고 간다.]')
else:
    print("[ 걸어가라.]")






# 빈 리스트 생성
# 예시! [미국, 영국, 프랑스, 중국]
cont = []

c1 = cont.append(input("나라를 입력해주세요:  "))
c2 = cont.append(input("나라를 입력해주세요:  "))
c3 = cont.append(input("나라를 입력해주세요:  "))
c4 = cont.append(input("나라를 입력해주세요:  "))

print("선택된 나라: {}".format(cont))

# 또 다른 방법
a1 = input("나라를 입력해주세요:  ")
a2 = input("나라를 입력해주세요:  ")
a3 = input("나라를 입력해주세요:  ")
a4 = input("나라를 입력해주세요:  ")
cont1 = [a1,a2,a3,a4]

print("선택된 나라: {}".format(cont1))
print("선택된 나라: [{}-{}-{}-{}]".format(a1,a2,a3,a4))
print("선택된 나라: [{}-{}-{}-{}]".format(cont1[0],cont1[1],cont1[2],cont1[3]))

f = [] # 과일 리스트
# 내가 입력힌 과일들로 리스트를 채워보세요! 과일 3개 이상

f1 = input("과일을 입력하세요:  ")
f2 = input("과일을 입력하세요:  ")
f3 = input("과일을 입력하세요:  ")
f4 = input("과일을 입력하세요:  ")

f.append(f1)
f.append(f2)
f.append(f3)
f.append(f4)

print("내가 좋아하는 과일은 {}, {}, {}, {} 입니다!!!".format(f[0],f[1],f[2],f[3]))

 

print("안녕하세요 제 이름은 홍길동입니다.")
print("저는 21살 입니다.")

# 홍길동 대신 이순신으로, 21 대신 30으로 바꾸고 싶을 경우
print("안녕하세요 제 이름은 이순신입니다.")
print("저는 30살 입니다.")

print("안녕하세요 제 이름은","홍길동","입니다.")
print("저는",30,"살 입니다.")

name = "이순신"
age = 30
print("안녕하세요 제 이름은",name,"입니다.")
print("저는",age,"살 입니다.")

# 변수 입력
a1 = "hello"
print(a1)
b1 = 2
print(b1)
a2 = "world"
print(a1,a2)
print(a1+a2)
print(a1+' '+a2)

c4 = 100
c3 = c4 # C4=100 이라서 c3는 100이 됨
c2 = c3 # c2 = 100
c1 = c2 # c1 = 100
print("c1 :" , c1)
c4 = 200 # 앞서 100에서 200으로 바꿈
print("c4 :", c4)
print("c1 :", c1)

# 변수를 이요해서 다음 문장을 출력해보세요
# 변수명 : fruit
# "포도", "딸기", "수박"순으로 입력
# 출력문장 >> 나는 00을 좋아합니다.
fruit1 = "포도"
fruit2 = "딸기"
fruit3 = "수박"
print("나는",fruit1+"를 좋아합니다.")
print("나는",fruit2+"를 좋아합니다.")
print("나는",fruit3+"을 좋아합니다.")
print("나는 {}를 좋아합니다.".format(fruit1))

# 변수명 : city
# 출력할 문장 : 나는 서울시에 살고 있습니다.
city1 = "서울시"
city2 = "전주시"
print("나는",city1+"에 살고 있습니다.")
print("나는",city2+"에 살고 있습니다.")
print("나는 {}에 살고 있습니다.".format(city1)) # ** 띄어쓰기를 하기 위해서 ,와 +를 사용하지 않고도 쓸 수 있다..

# 변수명: animal
# 출력할 문장: 나는 강아지를 키우고 있습니다.
animal1 = "강아지"
animal2 = "고양이"
print("나는 {}를 키우고 있습니다.".format(animal1))
print("나는 {}를 키우고 있습니다.".format(animal2))
# 출력할 문장: 강아지가 제일 좋아요.
print("{}가 제일 좋아요".format(animal1))
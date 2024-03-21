# 변수 3개를 만들어서 name, city, fruit
# 아래와 같이 출력해보세요.
# 저의 이름은 name 입니다.
# 저는 city에서 태어났습니다.
# 저는 fruit를 좋아합니다.

#1) 그냥 출력해보기
print("저의 이름은 홍길동 입니다.")
print("저는 부산시에서 태어났습니다.")
print("저는 딸기를 좋아합니다.")

#2) 변수를 선언해서 출력해보기
name = "홍길동"
city = "부산시"
fruit = "딸기"
print("안녕하세요.\n제 이름은",name,"입니다.","\n저는",city+"에서 태어났습니다.","\n저는",fruit+"을 좋아합니다.")
print("안녕하세요.\n제 이름은 %s입니다.\n저는 %s에서 태어났습니다.\n저는 %s을 좋아합니다."%(name,city,fruit))
print("안녕하세요.\n제 이름은 {}입니다. \n저는 {}에서 태어났습니다.\n저는 {}을 좋아합니다.".format(name,city,fruit))

#3) input을 사용하여 입력값을 받아서 출력해보기
name1 = input("이름을 작성하세요: ")
city1 = input("태어난 곳이 어디인가요?: ")
fruit1 = input("좋아하는 과일을 말해주세요: ")
print("안녕하세요. 제 이름은",name1,"입니다.")
print("저는",city1+"에서 태어났습니다.")
print("제가 좋아하는 과일은",fruit1+"입니다.")

# input()
inputVal = input("입력하시오 >> ")
print("입력하신 글자는 "+inputVal)
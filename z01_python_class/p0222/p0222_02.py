# 변수사용
# 변수 bool, int, float, str 형이 있다.
# 변수는 대소문자를 구분한다.(대문자는 주로 클래스에서 사용)
myVar = 10
MyVar = 20

# 변수는 언더바를 포함할 수 있고 숫자로 시작하면 안된다.
number1 = 10
my_number = 20
# 1number = 20 # 오류로 뜸

# 변수는 예약어를 사용할 수 없다.
# if = 100 
# True = 100

# 변수는 마지막으로 입력된 값을 저장한다. 코는 위에서 아래로 순차적으로 읽어나가는 성격을 가짐
a = 10
a = 30 

print(a) # 30

a = 1
b = 2
c = 3
print(1+2+3)
print(a+b+c)

var2 = 200
var1 = var2 + 100
print(var1, var2)

a = 1
b = 2
a, b =1, 2

# 입력 받기
# input()   : 입력을 받는 함수

name = input("이름을 입력하세요:  ")
print("당신의 이름은 "+name,"입니다.")

# # input()은 문자열로 입력이 된다.
# # 사칙연산을 하고 싶을 땐 숫자로 바꿔주는 작업 필수
age = int(input("나이를 입력하세요:  "))
print('당신은 내년에 {}살 입니다.'.format(age+1))

#  해보세요
# 숫자 하나를 입력받아서 구구단을 출력해보세요
# 2를 입력 받으면
# 2*1 = 2
# 2*2 = 4
# 2*3 = 6
number = int(input("숫자 하나를 입력해주세요:  "))
print("{} * 1 =".format(number),number*1)
print("{} * 2 =".format(number),number*2)
print("{} * 3 =".format(number),number*3)


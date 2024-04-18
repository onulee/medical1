# print("a는 %s입니다"%"입력값")
# a = "입력값"
# print("a는 %s입니다."%a)

#  입력함수 : input() => 문자열로 입력받는다.
# a = input("값을 입력해주세요 >> ")
# print("a는 %s입니다"%a)

n1 = int(input("첫 번째 숫자를 입력하세요 >> "))
n2 = int(input("두 번째 숫자를 입력하세요 >> "))
# 문자열로 인식이 되어있다.
# 이를 숫자(정수)로 바꿔주기 위해선 int를 사용
print("두 수의 합 : ", int(n1)+int(n2))
print("두 수의 차: ", int(n1)-int(n2))

a = 10 # 숫자
b = "10" # 문자
print("숫자일때 : ",a)
print("문자일때 : ",b)
# print("두 수의 합: ",a+b) # 오류
print("두 수의 합: ",a+int(b))


# 강제 형변환
# int 정수형
# float 실수형
# str 문자형
# bool 논리 자료형

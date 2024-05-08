# 산술 연산자
# +,-,*,/
a = 5
b = 3
result = a + b
print(result)

result = a // b # 몫을 구해주는 산술 연산자 몫:2 나머지:0
print(result)
result = a%b # 나머지를 구해줌
print(result)
result = a**b # 제곱근
print(result)

c = 10
d = 10
c,d = 100, 200

# 산술연산자 우선순위
# 곱셈, 나눗셈 먼저 -> 덧셈, 뺄셈 순으로 진행
# 괄호가 없을 경우 왼쪽에서 오른쪽으로 계산
r1 = 2 + 2 - 2 * 2 / 2 * 2

# 괄호사용을 추천합니다. 보면 헷갈리기 때문!
r2 = 2 - (2/2)

# 다른 자료형으로 연산
str1 = "문자열"
n1 = 10

print(str1*n1)
# print(str1+n1) # error

# 문자열이 정수나 실수일 경우 int() float()를 사용해서 변환
s1 = "100"
s2 = "10.123"
print(int(s1)+1)
print(float(s2)+1)

# 숫자가 아닌 것을 변환할 수 없다.
# n = int("안녕하세요") # error

n1 = 100
n2 = 10.123
print(str(n1)+"1")
print(str(n2)+"1")

p = 12341234
print("010"+str(p))


# 숫자 두 개를 입력 받아서 나누기, 몫, 나머지 값을 구하세요
n1 = int(input("첫 번째 숫자:  "))
n2 = int(input("두 번째 숫자:  "))
print("나누기 값: {}\n몫: {}\n나머지: {}".format(n1/n2,n1//n2,n1%n2))
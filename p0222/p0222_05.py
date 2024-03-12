# 국어, 영어, 수학 점수를 입력 받아서 평균을 출력하세요
# 출력: 평균은 95 점 입니다.
# 변수: kor, eng, math

# 단순 변수 지정
kor1 = 100
eng1 = 90
math1 = 80

print("평균은 {}점 입니다.".format((kor1+eng1+math1)/3))

# # input 함수를 사용하여 입력값 받기
kor = int(input("국어 점수를 입력해주세요:  "))
eng = int(input("영어 점수를 입력해주세요:  "))
math = int(input("수학 점수를 입력해주세요:  "))

print("평균은 {}점 입니다.".format((kor+eng+math)/3))

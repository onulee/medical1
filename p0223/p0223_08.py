# 점수를 입력 받아서
# 90점 이상이면 A
# 80점 이상이면 B
# 70점 이상이면 C, 나머지는 F를 출력해보세요

# 98점 이상이면 A+, 90-93 사이는 A-
# B+... 등등

name = input("이름을 입력해주세요:  ")
score = int(input("점수를 입력해주세요:  "))

if score >= 90:
    if score >= 98:
        print("{}님의 성적은 A+ 입니다.".format(name))
    elif score >= 94:
        print("{}님의 성적은 A0 입니다.".format(name))
    else:
        print("{}님의 성적은 A- 입니다.".format(name))
elif score >= 80:
    if score >= 88:
        print("{}님의 성적은 B+ 입니다.".format(name))
    elif score >= 84:
        print("{}님의 성적은 B0 입니다.".format(name))
    else:
        print("{}님의 성적은 B- 입니다.".format(name))
elif score >= 70:
    if score >= 78:
        print("{}님의 성적은 C+ 입니다.".format(name))
    elif score >= 74:
        print("{}님의 성적은 C0 입니다.".format(name))
    else:
        print("{}님의 성적은 C- 입니다.".format(name))
else:
    print("{}님의 성적은 F 입니다.".format(name))
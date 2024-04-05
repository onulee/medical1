# 12,1,2월 겨울 3,4,5월 봄 6,7,8월 여름 9,10,11월 가을
# 1월, 2월, 3월.....12월

# 1 - 겨울입니다.
# 12 - 겨울입니다.
# 7 - 여름입니다.

season3 = input("월을 입력하세요.")
print(season3)
season2 = season3[0:-1]
print(season2)

season = int(season2)

if 3<= season <=5:
    print("봄입니다.")
elif 6<= season <=8:
    print("여름입니다.")
elif 9<= season <=11:    
    print("가을입니다.")
elif season==12 or 1<= season <=2:
    print("겨울입니다.")
        
        
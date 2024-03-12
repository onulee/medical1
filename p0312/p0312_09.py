def para_func(*num): # 가변매개변수
    # print(num)
    sum = 0
    for n in num:
        sum += n
    print("합계 : ",sum)    

# 함수를 1,2,3,4,5,6,7,8,9,10
# 더하기 결과값을 출력하시오.
para_func(1,2)
para_func(1,2,3)
para_func(1,2,3,4)
para_func(1,2,3,4,5)
para_func(1,2,3,4,5,6)
para_func(1,2,3,4,5,6,7)
para_func(1,2,3,4,5,6,7,8)
para_func(1,2,3,4,5,6,7,8,9)
para_func(1,2,3,4,5,6,7,8,9,10)
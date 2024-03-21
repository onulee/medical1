# 콜백함수

# 함수선언 - 콜백함수
def callback_func(h_print):
    for i in range(10):
        h_print(i)

# 함수선언
def h_print(num):
   print("안녕하세요.",num)
   
# 함수호출 - 매개변수로 함수를 넘겨주는 것을 콜백함수 
callback_func(h_print)   




#----------------------
# 함수호출
# h_print()    

# 함수를 변수에 저장
# func = h_print




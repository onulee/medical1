# 재귀함수
def count(num):
    if num>=1:
        print(num,end=" ")
        count(num-1) #자신의 함수를 다시 호출 : 재귀함수
    else :
        return
    
count(10)  

# for i in range(10,0,-1):
#     print(i,end=" ")
    

     
a_tu = (1,2,3)
print(a_tu)
print(a_tu[0])

print(list(a_tu))


# # 함수
# # 가변매개변수 : *b
# def func(a,*b): # 매개변수 개수:2개, 튜플:리스트타입인데 수정,삭제가 불가능
#     print(a)
#     for i in b:
#         print(i)
    
# func(1,2,3,4,5,6,7,8,9,10) # 매개변수 4개   



# print("{:05d},{:.2f}".format(1,2.484874747,3))

# a_list = [1,2,3,4,5] # 튜플 (1,2,3,4,5)
# print(a_list)
# print(*a_list)

# print("{},{},{},{},{}".format(a_list[0],a_list[1],a_list[2],a_list[3],a_list[4]))
# print("{},{},{},{},{}".format(*a_list))


# a = "123"
# if a.isdigit():
#     a = int(a)
# else:
#     print("숫자가 아닙니다")
    
# print(type(a))            
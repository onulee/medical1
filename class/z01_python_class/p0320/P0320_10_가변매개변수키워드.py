def func(n,*val,a=2):
    for i in range(n):
        for v in val:
            print(v)


func(1,"안녕","안녕하세요.","반갑습니다","매개변수")

print(5,4,3,2,1,sep=",",end="")

# a_dic = {
#     "a":"홍길동",
#     "b":"유관순",
#     "c":"이순신"
# }

# for key in a_dic:
#     print(a_dic[key])
# for key in a_dic.keys():
#     print(key)
# for val in a_dic.values():
#     print(val)
# for k,v in a_dic.items():
#     print(k,v)


# print(range(10))
# a = range(10)
# print(a)

# print(list(range(10)))

# print([ i for i in range(10)])

# for i in range(1,10+1,2):
#     print(i)
    
# for i in range(10,1-1,-1):
#     print(i)
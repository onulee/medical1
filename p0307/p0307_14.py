list = [1,2,3]
# alist = list #공간같이 쓴다.
alist = [*list] #1
alist = list[:] #2
list[0] = 100

print(alist)

a = 100
b = a
a = 10
print(b) # 100
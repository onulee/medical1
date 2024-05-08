# 리스트
# list = [1,2,3,4,5,6,7,8,9,10]

# 1-10까지 입력해보세요.
# 1.list 기본문법
list = []
for i in range(1,11):
    list.append(i)

list = [0]*10  #2. 공간을 먼저 만들고
for i in range(0,10):
    list[i] = i+1
print(list)    

# 3. 컴프리헨션
# list = [i for i in range(1,11)]
# print(list)    
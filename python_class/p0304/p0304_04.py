students = [['홍길동',100,100,99,299,99,97],\
    ['유관순',100,100,99,299,99,99.97],
    ['이순신',100,100,99,299,99,99,97]]

kors = 0
# students는 2차원 배월
#stu는 1차원 배열
for i, stu in enumerate(students):
    kors += stu[1]
    
print(kors)
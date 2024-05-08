str1 = "1,'홍길동',100,100,100,300,100.0"
s_list = str1.split(",")
# print(s_list)

students = []
s_dic = { "stuNo":int(s_list[0]),"name":s_list[1],
    "kor":int(s_list[2]),"eng":int(s_list[3]),
    "math":int(s_list[4]),"total":int(s_list[5]),
    "avg":float(s_list[6]) }

students.append(s_dic)

print(students)
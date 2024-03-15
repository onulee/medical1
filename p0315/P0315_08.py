# stu.txt 파일을 읽어 출력하시오.
students = [] # 전체학생의 리스트
with open("stu.txt","r",encoding="utf8") as f:
    while True:
        txt = f.readline() # 1줄씩 읽기
        if txt == "": break
        t_list = txt.split(",") #csv파일을 ,분리
        # print("{},{},{},{},{},{},{}".format(*t_list))
        s_dic = {
            "stuNo":int(t_list[0]),"name":t_list[1],
            "kor":int(t_list[2]),"eng":int(t_list[3]),"math":int(t_list[4]),
            "total":int(t_list[5]),"avg":float(t_list[6]),"rank":int(t_list[7])
        }
        # 
        students.append(s_dic)
        # print("{},{},{},{},{},{},{}".format(*t_list))
print(students[0]["name"])        
        
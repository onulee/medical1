# '''
# 변수명 : stu_no, stu_name, kor, eng, math, total, avg, rank
# 출력 :
stu_no = input("학생 번호를 작성하세요: ")
stu_name = input("이름을 작성하세요: ")
kor = int(input("국어 성적: "))
eng = int(input("영어 성적: "))
math = int(input("수학 성적: "))
total = int(kor+eng+math)
avg = int((kor+eng+math)/3)
rank = "1"


print("""{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format("번호","이름","국어","영어","수학","합계","평균","등수")
,"{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(stu_no,stu_name,kor,eng,math,total,avg,rank)""")
import oracledb

# sql
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() #db와 연결되어 지시자 생성

# sql구문을 통해 가져온 데이터 중
# 평균을 가지고 파이썬에서 프로그램하여 학점을 출력하시오.
# 학번,이름,합계,평균,학점
sql = "select * from stu_score"



cursor.execute(sql)      # cursor에 select한 결과값을 저장(결과값 : list)
data = cursor.fetchall() # fetchall():모든 데이터 가져옴. fetchone() : 1개의 데이터 가져옴.

print("[ 모든 데이터 출력 ]")
# print(data)
for d in data[:5]:
    # print(d)
    print("평균 : ",d[6])
    if d[6]>=90:
        print("grade : ","A")
    elif d[6]>=80:
        print("grade : ","B")
    elif d[6]>=70:
        print("grade : ","C")
    elif d[6]>=60:
        print("grade : ","D")
    else:
        print("grade : ","F")
        
    print("-"*20)
print("-")
print("타입 : ",type(data))


# salary 그룹함수 평균을 출력하시오.
sql = "select round(avg(salary),2) as salary from employees"
cursor.execute(sql)
data = cursor.fetchone() # 데이터 결과값이 1개일때
print(data[0])


conn.close() # 데이터베이스 연결해제

# sql = '''select no, name,total, avg,
# case 
# when avg>=90 then 'A'
# when avg>=80 then 'B'
# when avg>=70 then 'C'
# else 'F'
# end as grade
# from stu_score '''









        
# sql = "select bno,a.id,name,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile \
#         from board a,member b \
#         where a.id = b.id "        

# stu_score avg 90점 이상 A, 80이상 B,C,D, 60점 미만 F
# 학번,이름,합계,평균,학점 출력하시오.


# board테이블 id포함 모든 컬럼, member테이블의 name컬럼을 가져와 출력하시오.
# board테이블 id, member테이블 name
# sql = "select bno,a.id,name,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile \
#         from board a,member b \
#         where a.id = b.id"





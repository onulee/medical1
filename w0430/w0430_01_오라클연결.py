import oracledb

# sql
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() #db와 연결되어 지시자 생성

# 이름 2번째 a가 있는 학생을 학번으로 순차정렬해서 출력하시오. 
sql = "select * from stu_score where name like '_a%' order by no asc"
cursor.execute(sql)      # cursor에 select한 결과값을 저장(결과값 : list)
data = cursor.fetchall() # fetchall():모든 데이터 가져옴. fetchone() : 1개의 데이터 가져옴.

print("[ 모든 데이터 출력 ]")
# print(data)
for d in data:
    print(d)
    # print("학번 : ",d[0])
    # print("이름 : ",d[1])
    # print("국어 : ",d[2])
    # print("영어 : ",d[3])
    # print("수학 : ",d[4])
    print("-"*20)
print("-")
print("타입 : ",type(data))




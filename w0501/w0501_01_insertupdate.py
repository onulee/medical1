import oracledb

conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() # 커서생성 - 명령어 입력받는 함수

# insert,update,delete 
# sql = "insert into member values ( member_seq.nextval,'ggg',1111,'홍길순','여자',sysdate )"
# sql="update member set name='홍길동' where id='aaa'"
# cursor.execute(sql)
# cursor.execute('commit')


# select 읽어오기
# fetchone(),fetchall()
sql = "select * from member"
cursor.execute(sql)
data = cursor.fetchall()

for d in data:
    print(d)


cursor.close()
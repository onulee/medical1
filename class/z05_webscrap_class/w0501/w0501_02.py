import oracledb

# 데이터베이스 연결 함수
def connection():
    conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
    cursor = conn.cursor() # 커서생성 - 명령어 입력받는 함수
    return cursor

    
# 실행    
sql = "select * from member"
cursor = connection()
cursor.execute(sql)
data = cursor.fetchall()

for d in data:
    print(d)


cursor.close()
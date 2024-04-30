import oracledb

conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()


# 프로그램을 반복하는 형태로 구성하고, -1을 입력하면 종료되도록 하시오.

while True:
    # 검색어 입력부분
    search = input("찾고자 하는 이름을 입력하세요.>>")
    if search == '-1':
        break
    
    # 검색부분
    sql = f"select * from stu_score where name like '%{search}%'"
    # sql = "select * from stu_score where name like '%{}%'".format(search)
    cursor.execute(sql)
    data = cursor.fetchall()

    for d in data:
        print(d)
    print("-"*30)
    print("검색된 데이터 개수 : ",len(data))
    print()

    
print("프로그램을 종료합니다.")
conn.close()    
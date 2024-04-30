import oracledb

# 점수를 입력받아 입력한 평균점수 이상,이하를 선택해서 학생을 출력하시오.
# 반복해서 진행하고 -1을 입력받으면 프로그램을 종료하시오.

while True:
    conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
    cursor = conn.cursor()
    search = input("평균점수를 입력하세요.(-1:종료)>>")
    if search == '-1':
        break
    
    print("1. 점수이상")
    print("2. 점수미만")
    num_str = input("점수이상 또는 이하를 선택하세요.>>")
    if num_str == '1':
        sql = f"select * from stu_score where avg>={search} order by no"
    else:
        sql = f"select * from stu_score where avg<{search} order by no"
            
    cursor.execute(sql)
    data = cursor.fetchall()

    for d in data:
        print(d)
        
    print("-"*30)
    print("검색된 데이터 개수 : ",len(data))
    print()
    conn.close() 
    
print("프로그램을 종료합니다.")
conn.close()     
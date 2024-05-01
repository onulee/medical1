import oracledb

# 데이터베이스 연결 함수
def connection():
    conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
    cursor = conn.cursor() # 커서생성 - 명령어 입력받는 함수
    return conn,cursor

def close(cursor,conn):
    cursor.close()
    conn.close()
 
# employees 이름으로 검색하는 부분 로직을 구현하시오.
# 무한반복, -1 프로그램 종료

while True:
    print("1. 이름으로 검색")
    print("2. 이름으로 같은 부서에서 근무하는 사원 조회")
    choice = input("원하는 번호를 입력하세요. >> ")
    if choice == '-1':
        break
    elif choice == '1':
        search = input("이름을 입력하세요. >> ")
        print("-"*30)
        sql = f"select * from employees where emp_name like '%{search}%'"
        conn,cursor = connection()
        cursor.execute(sql)
        data = cursor.fetchall()
        for d in data:
            print(d[0],end="\t")
            print(d[1],end="\t")
            print(d[4],end="\t")
            print(d[5],end="\t")
            print(d[6],end="\t")
            print(d[9])
        
        print("-"*30)
        print()
        
    elif choice == '2':
        search = input("이름으로 함께 근무하는 사원을 검색합니다. 이름을 입력하세요. >> ")
        #### 프로그램 구현
        sql = f'''select b.employee_id,a.department_id,c.department_name,b.emp_name from employees a,employees b,departments c
                 where a.department_id = b.department_id and a.emp_name = '{search}'
                 and a.department_id = c.department_id
              '''
        conn,cursor = connection()
        cursor.execute(sql)
        data = cursor.fetchall()
        for d in data:
            print(d[0],end="\t")
            print(d[1],end="\t")
            print(d[2],end="\t")
            print(d[3])
        print("-"*30)
        print()
    
    # db연결 해제
    close(cursor,conn)    

print("[ 프로그램 종료합니다. ]")    
 
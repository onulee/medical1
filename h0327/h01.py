while True:
    print("[ 로그인 ]")
    print("-"*20)
    id = input("아이디 : ")
    pw = input("패스워드 : ")
    print("-"*20)
    
    # 파일에서 아이디와 패스워드 확인 (데이터베이스에서 확인)
    chk = 0
    with open("member.csv","r",encoding="utf-8") as f:
        while True:
            txt = f.readline()
            if txt=="": break
            mem = txt.split(",")
            # 아이디,패스워드 비교
            if id==mem[1] and pw==mem[2]:
                chk = 1
                break
    
    # id,pw가 없으면 chk==0, id,pw가 있으면 chk==1            
    if chk==1:
        print("로그인이 되었습니다.")
        break
    else:
        print("아이디 또는 패스워드가 일치하지 않습니다.\
              \n다시 입력하세요.")    

while True:
    print("[ 학생성적 프로그램 ]")        
    print("-"*30)
    print("1. 학생성적입력")
    print("0. 종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    if choice == 1:
        print("학생성적입력을 진행합니다.")
    elif choice == 0:
        print("프로그램을 종료합니다.")
        break
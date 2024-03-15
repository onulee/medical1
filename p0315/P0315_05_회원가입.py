while True:
    print("-"*40)
    print("[ 회원정보 ]")
    print("-"*40)
    print("1. 회원가입")
    print("2. 로그인")
    print("3. 회원정보수정")
    print("-"*40)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    
    if choice == 1: # 회원가입
        # mem.txt를 가지고 로그인을 구현하시오.
        print("-"*42)
        print("\t\t[ 회원가입 ]")
        print("-"*42)
        print("* 회원정보를 입력해주세요. ")
        print()
        c_id = input("ID를 입력하세요.>> ")
        c_pw = input("PASSWORD를 입력하세요.(0.종료)>> ")
        
        # 파일추가
        # 파일열기
        f = open("mem.txt","a",encoding="utf8")
        f.write(f"{c_id},{c_pw}\n")
        f.close()
        
        print("회원가입을 축하합니다.")
        print()
        
    elif choice == 2:
        # mem.txt를 가지고 로그인을 구현하시오.
        print("-"*42)
        print("\t\t[ 로그인 ]")
        print("-"*42)
        print("* 먼저 로그인을 해주세요.")
        print()
        c_id = input("ID를 입력하세요.>> ")
        c_pw = input("PASSWORD를 입력하세요.(0.종료)>> ")
        
        if c_pw == "0": break # 0.종료
        # 파일열기
        f = open("mem.txt","r",encoding="utf8")
        # 파일읽기
        success_flag = 0 
        while True:
            txt = f.readline()
            if txt == "": break
            t_list = txt.split(",")
            t_list[0] = t_list[0].strip()    
            t_list[1] = t_list[1].strip()  
            if c_id == t_list[0] and c_pw == t_list[1]:
                  success_flag = 1
                  break
        
        if success_flag == 1:
            print("로그인이 되었습니다.")  
            print()
            print("[ 학생성적 프로그램 시작 ]")
            print()
                
        else:
            print("아이디 또는 패스워드가 일치하지 않습니다. 다시 로그인해주세요.")
        
        
    elif choice == 3:
        # 파일에 있는 모든 정보를 list에 저장
        member = []
        f = open("mem.txt","r",encoding="utf8")
        while True:
            txt = f.readline()
            if txt == "": break
            t_list =txt.split(",")
            t_list[0] = t_list[0].strip()
            t_list[1] = t_list[1].strip()
            member.append([t_list[0],t_list[1]])
        
        print("[ 회원정보수정] ")
        search = input("수정하려는 ID를 입력하세요.>> ")
        cnt = 0 # 동일한 ID가 있는 위치 확인변수
        for m in member:
            if search == m[0]: # 동일한 ID가 있는지 확인
                break
            cnt += 1
            
        if cnt == len(member):
            print("아이디가 존재하지 않습니다. 다시 입력하세요.")   
        else:
            print("아이디를 찾았습니다.!!")
            print()
            print("[ 패스워드 수정 ]")     
            pw_input = input("수정할 패스워드를 입력하세요.>> ")
            member[cnt][1] = pw_input
            
            # list의 모든 파일을 저장
            f = open("mem.txt","w",encoding="utf8")
            for m in member:
                f.write(f"{m[0]},{m[1]}\n")
            f.close()    
                     
            
            
            
        

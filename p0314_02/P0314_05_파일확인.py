import os

while True:
    print("[ 윈도우 탐색기 ]")
    print("-"*40)
    print("1. 폴더 내 파일 확인")
    print("2. 파일 불러오기")
    print("3. 파일 저장")
    print("-"*40)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    
    if choice == 1:
        print("[ 폴더 내 파일 ]")
        print(os.listdir()) # 1개씩 세로로 출력되도록 하시오.
        for f_name in os.listdir():
            # if f_name.find('.') == -1:
            if f_name.endswith('.txt'):
                print(f_name)
        
    elif choice == 2:
        # txt파일만 출력해서 입력을 받아보세요.
        print("[ 파일 불러오기 ]")
        for f_name in os.listdir():
            # if f_name.find('.') == -1:
            if f_name.endswith('.txt'):
                print(f_name)
        print("-"*40)
        search = input("파일명을 입력하세요.>> ")
        
        # 파일 열기
        f = open(search,"r",encoding="utf8")
        
        # 파일 읽기
        while True:
            content = f.readline()
            if content == "": break
            print(content,end="")
        print()
        
        # 파일 닫기
        f.close()
        
        
    elif choice == 3:
        # txt파일만 출력해서 입력을 받아보세요.
        print("[ 파일 저장하기 ]")
        print("1. 기존파일에 저장하기")
        print("2. 새로운파일 저장하기")
        choice = int(input("원하는 번호를 입력하세요.>> "))
        if choice == 1:
            for f_name in os.listdir():
                # if f_name.find('.') == -1:
                if f_name.endswith('.txt'):
                    print(f_name)
            print("-"*40)
            search = input("해당 파일명을 입력하세요.>> ")
        
            # 파일 열기
            f = open(search,"a",encoding="utf8")
            print("[ 아래 글을 입력하세요 ]")
            # 파일 쓰기
            while True:
                txt_input = input('')
                if txt_input == "-1": break
                f.write(txt_input+"\n") #줄바꿈
            
            # 파일 닫기
            print("파일에 글자를 저장했습니다.")
            f.close()
            
        elif choice == 2:    
            print("-"*40)
            search = input("신규 파일명을 입력하세요.>> ")
        
            # 파일 열기
            f = open(search,"w",encoding="utf8")
            print("[ 아래 글을 입력하세요 ]")
            # 파일 쓰기
            while True:
                txt_input = input('')
                if txt_input == "-1": break
                f.write(txt_input+"\n")
            
            # 파일 닫기
            print("파일에 글자를 저장했습니다.")
            f.close()
            
            
    
    
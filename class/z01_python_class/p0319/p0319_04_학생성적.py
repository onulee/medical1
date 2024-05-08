#-----------------------------
# Student클래스
#-----------------------------
class Student:
    count = 1 # 클래스 변수 사용
    
    def __init__(self,name,kor,eng,math,stuNo=0,rank=0):
        if stuNo == 0:
            self.stuNo = Student.count  # 클래스변수 사용
        else:
            self.stuNo = stuNo    
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = float("{:.2f}".format(self.total/3))
        self.rank = rank   
    
    def __str__(self): #객체를 호출하면 출력됨.
        return f"{self.stuNo}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}" 

#-----------------------------
# 파일 불러와서 저장하기
#-----------------------------
students = []
f = open("stu.txt","r",encoding="utf8")
while True:
    txt = f.readline()
    if txt == "": break
    txt_list = txt.split(",")
    # 1,홍길동,99,99,87,285,95.0,1
    s = Student(txt_list[1],int(txt_list[2]),int(txt_list[3]),int(txt_list[4]),int(txt_list[0]),int(txt_list[7]))
    students.append(s)
f.close() 

# 파일 불러오기 한후 학생수에서 +1추가
Student.count = len(students)+1 

search_txt = [
                "",
                "찾고자 하는 학생 이름을 입력하세요.>> ",
                "몇 점이상 검색하시겠습니까?>> ",
                "몇 점이하 검색하시겠습니까?>> "
            ]
#-----------------------------
# 함수부분
#-----------------------------

def main_title_print():
    print("-"*40)
    print("[ 학생성적프로그램 ]")
    print("-"*40)
    print("1. 학생성적입력")
    print("2. 학생성적전체입력")
    print("3. 학생검색")
    print("4. 학생성적수정")
    print("5. 학생성적삭제")
    print("6. 등수처리")
    print("0. 종료")
    print("-"*40)
    choice = input("원하는 번호를 입력하세요.>> ")
    choice = int(choice)
    return choice

def stu_main_print():
    print('\t[ 학생성적출력 ]')
    print('-'*65)
    print('학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
    print('-'*65)

def stu_insert():
    while True :
        name = input(f"{len(students)+1}번째 학생의 이름을 입력하세요.(0.취소)")
        if(name=="0"):
            print("학생 입력을 취소합니다.")
            break
        kor = int(input("국어점수를 입력하세요."))
        eng = int(input("영어점수를 입력하세요."))
        math = int(input("수학점수를 입력하세요."))
        # list에 추가
        s = Student(name,kor,eng,math)
        students.append(s)
        print("입력 데이터 :",s) 
        
def stu_print():
    stu_main_print()
    # 데이터 출력
    for i in students:
        print(i) # 객체를 출력
    print()
    
def search_title_print():
    print("\t[ 학생성적 검색 ]")
    print("-"*40)
    print("1. 학생이름으로 검색")  
    print("2. 총점이상 검색")  
    print("3. 총점이하 검색")  
    print("0. 이전화면 이동")  
    choice = int(input("원하는 번호를 입력하세요.>> "))  
    return choice 

def stu_search(choice):
    if choice == 1:
        search = input(search_txt[choice])
    else:
        search = int(input(search_txt[choice]))
    # 전체리스트에서 학생검색
    s_list = []
    for i in students:
        if choice == 1:
            if i.name.find(search) != -1:
                s_list.append(i)
        elif choice == 2:
            if i.total >= search:
                s_list.append(i)
        elif choice == 3:
            if i.total <= search:
                s_list.append(i)        
    
    if len(s_list) != 0:
        stu_main_print()  
        for i in s_list:
            print(i)
    else:
        print("찾고자 하는 학생이 없습니다. 다시 검색하세요. ")              

def stu_update():
    search = input("찾고자 하는 이름을 입력하세요.>> ")
        
    # 전체리스트에서 학생검색
    cnt = 0
    for s in students: # 학생수만큼 반복 7명-> 7번반복
        if s.name == search: # 0,1,students[2],3,4,5,6
            break
        cnt += 1        
    
    if cnt >= len(students):
        print("찾고자 하는 학생이 없습니다. 다시 검색하세요. ") 
    else:
        print(f"{search} (으)로 검색한 학생을 찾았습니다.")   
        print()
        print("[ 수정할 과목 선택 ]")
        print("-"*30)
        print("1. 국어")
        print("2. 영어")
        print("3. 수학")
        print("-"*30)
        choice = int(input("원하는 번호를 입력하세요.>> "))
        
        if choice == 1:
            print(f"변경전 점수 : {students[cnt].kor}")
            students[cnt].kor = int(input("변경할 점수를 입력하세요.>> "))
            students[cnt].total = students[cnt].kor + students[cnt].eng + students[cnt].math
            students[cnt].avg = float("{:.2f}".format(students[cnt].total/3))
            print(f"{students[cnt].kor} 으로 점수가 변경되었습니다.")
        elif choice == 2:
            print(f"변경전 점수 : {students[cnt].eng}")
            students[cnt].eng = int(input("변경할 점수를 입력하세요.>> "))
            students[cnt].total = students[cnt].kor + students[cnt].eng + students[cnt].math
            students[cnt].avg = float("{:.2f}".format(students[cnt].total/3))
            print(f"{students[cnt].eng} 으로 점수가 변경되었습니다.") 
        elif choice == 3:
            print(f"변경전 점수 : {students[cnt].math}")
            students[cnt].math = int(input("변경할 점수를 입력하세요.>> "))
            students[cnt].total = students[cnt].kor + students[cnt].eng + students[cnt].math
            students[cnt].avg = float("{:.2f}".format(students[cnt].total/3))
            print(f"{students[cnt].math} 으로 점수가 변경되었습니다.") 

def stu_delete():
    search = input("삭제하고자 하는 학생이름을 입력하세요.>> ")
        
    # 전체리스트에서 학생검색
    cnt = 0
    for s in students: # 학생수만큼 반복 7명-> 7번반복
        if s.name == search: # 0,1,students[2],3,4,5,6
            break
        cnt += 1        
    
    if cnt >= len(students):
        print("찾고자 하는 학생이 없습니다. 다시 검색하세요. ") 
    else:
        print(f"{search} (으)로 검색한 학생을 찾았습니다.")   
        print()
        print("[ 학생성적 삭제선택 ]")
        print("-"*30)
        print("1. 삭제")
        print("0. 취소")
        choice = int(input("원하는 번호를 입력하세요.>> "))
        
        if choice == 1:
            del students[cnt]
            print(f"{search} 학생 성적이 삭제 되었습니다.")
        else:
            print("학생성적 삭제를 취소하셨습니다.")

def stu_rank():
    print("[ 등수처리 진행 ]")
    print("1. 진행")
    print("0. 취소")
    choice = int(input("원하는 번호를 입력하세요.>> "))
    
    if choice == 1:
        for s in students:
            rank_count = 1 #초기화
            for ss in students:
                if s.total<ss.total:
                    rank_count += 1 
                s.rank = rank_count
        print("등수처리가 완료되었습니다.")
        print()                       
    else:
        print("등수처리 진행을 취소하셨습니다.")


#-----------------------------
# 메인 프로그램 시작
#-----------------------------
    
# # 리스트 출력
while True:    
    choice = main_title_print() #메인화면
    
    # 프로그램
    if choice == 1: stu_insert()   # 학생성적입력
    elif choice == 2: stu_print()  # 학생성적전체출력
    elif choice == 3:              # 학생검색
        while True:
            choice = search_title_print()
            if choice == 0:
                print("이전화면으로 이동합니다.")
                print()
                break
            # 학생검색 프로그램 부분
            stu_search(choice)
    elif choice == 4: # 학생성적수정
        stu_update()
    elif choice == 5: # 학생성적삭제
        stu_delete()
    elif choice == 6: # 등수처리
        stu_rank()
    else: # 종료
        print("프로그램을 종료합니다.")
        break
                       
            
            
            
                
            
            
  
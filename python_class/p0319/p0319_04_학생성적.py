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

#-----------------------------
# 함수부분
#-----------------------------
search_txt = [
                "",
                "찾고자 하는 학생 이름을 입력하세요.>> ",
                "몇 점이상 검색하시겠습니까?>> ",
                "몇 점이하 검색하시겠습니까?>> "
            ]

def main_title_print():
    print("-"*40)
    print("[ 학생성적프로그램 ]")
    print("-"*40)
    print("1. 학생성적입력")
    print("2. 학생성적전체입력")
    print("3. 학생검색")
    print("4. 학생성적수정")
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
       # 1. 이름으로 학생을 검색
       # 2-1. 찾았으면 과목 선택
       # 2-1-1. 과목리스트 출력
       # 2-1-2. 국어선택
       # 2-1-3. 국어점수 출력 후 국어점수 입력
       # 2-1-4. 국어점수 변경후 이전화면 이동
       
       # 2-2. 못 찾았으면 다시 이전화면으로 나옴.     
            
            
                
            
            
  
class Student:
    stuCount = 0 # 클래스변수
    stuNo = 0    # 인스턴스변수 
        
    # 생성자 : __init__
    # 클래스에 대해 객체선언을 하면 제일먼저 호출되는 함수
    def __init__(self,name="",kor=0,eng=0,math=0): 
        self.name = name
        if kor>100:
            self.kor = 100
        else:
            self.kor = kor    
        
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = float("{:.2f}".format(self.total/3))
        self.rank = 0
        Student.stuCount += 1 # 클래스변수선언 - 클래스명.변수명
        self.stuNo = Student.stuCount
    
    def stu_print(self):
        print(self.stuNo,self.name,self.kor,self.eng,self.math \
            ,self.total,self.avg,self.rank,sep="\t")
    # 객체를 print하면 __str__함수를 제일먼저 호출함.
    def __str__(self):
        return f"{self.stuNo},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg},{self.rank}"
      

# 매개변수가 있는 객체(인스턴스)선언
s1 = Student("홍길동",200,100,99)  
s2 = Student("유관순",99,99,98)

print(s1)  # __str__ 함수호출 없으면 주소값 출력

        
            
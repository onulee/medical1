class Student:
    def __init__(self,name,total):
        self.name = name
        self.total = total
    # def __str__(self):
    #     return f"이름 : {self.name}, 총점 : {self.total}" 
    
    def __del__(self):
        return "클래스가 소멸될때 실행"  
    
    def __add__(self,s):
        return self.total+s.total 
    
    def __gt__(self,s):
        return self.total>s.total
    
    def __eq__(self,s):
        return self.name==s.name and self.total == s.total
            


# -------
s1 = Student("홍길동",100)
s2 = Student("유관순",90)
s3 = Student("이순신",95)
s4 = Student("홍길동",100)

print(s1)    # 클래스를 출력할때 str함수 호출
print(s1+s2) # 클래스를 더하기 할때 , add함수 호출

print(s1>s2) # 클래스는 비교가 불가능 한데, __gt__ 메소드를 생성하면 호출
print(s2>s3) # 클래스는 비교가 불가능 한데, __gt__ 메소드를 생성하면 호출

print(s1)
print(s4)
print("s1==s4 : ",s1==s4)
print("s1==s2 : ",s1==s2)
    
        
# 클래스 : 사용자정의 변수 - 함수도 포함
# 클래스 첫글자 대문자 사용
# 클래스 : 설계도

# 클래스 선언
class Car:
    color = "white"
    door = 5
    length = 4710
    width = 1800
    displace = 1600
    speed = 0
    
    def upSpeed(self,sp):
        self.speed += sp
        
    def downSpeed(self,sp):
        self.speed -= sp    
    
# 객체선언을 할때마다 제품(Car)이 한개씩 생산
c1 = Car() # 객체선언
print("색상 : ",c1.color)
c1.color = "red"
print("변경후 색상 : ",c1.color)

c2 = Car()
print("색상 : ",c2.color)



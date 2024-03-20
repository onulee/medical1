class Car:
    count = 0
    
    def __init__(self,color="red",door=5,tire=4,speed=0):
        self.color = color
        self.door = door
        self.tire = tire
        self.speed = speed
    
    def up_speed(self):
        self.speed += 10
        
    def down_speed(self):
        self.speed -= 10
    
    def stop_speed(self):
        self.speed -= 10    
        
# Car클래스 상속
class Ambul_car(Car):
    # Car클래스의 모든 것을 가져옴
    def up_speed(self): # 자식클래스에서 오버라이딩 된 함수
        self.speed += 20
        # return super().up_speed()
        
    def up_speed2(self): # 기존 부모의 함수를 다시 호출 하고 싶을때
        return super().up_speed() # 부모의 요소를 가져올때 super()
        
    
    def siren(self):
        print("싸이렌이 울리는 기능이 추가 됩니다.")  

        
class FireTruck_car(Car):
    def water(self):
        print("물을 뿌리는 기능이 추가 됩니다.")          
                   

a1 = Ambul_car()
print("현재속도 : ",a1.speed)  
a1.up_speed() # 자식의 오버라이딩 된 함수를 호출
print("현재속도 : ",a1.speed)  
a1.up_speed2() # 부모의 함수를 호출해서 사용
print("현재속도 : ",a1.speed)  

a1.stop_speed()
print("현재속도 : ",a1.speed)  
print("앰블런스 색상 : ",a1.color)

      
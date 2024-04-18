class Car:
    car_name = ""
    color = ""
    door = 0
    length = 0
    width = 0
    speed = 0
    
    # 생성자
    def __init__(self,car_name="",color="",door=5,length=1000,width=1000,speed=0):
        self.car_name = car_name
        self.color = color
        self.door = door
        self.length = length
        self.width = width
        self.speed = speed
    
    def up_speed(self,s):
        self.speed += s 

# 기본생성자를 사용한 객체선언
c4 = Car() 
c4.car_name = "드뉴아반떼"
c4.color = "white"
c4.door = 5
c4.length = 2000
c4.width = 1000
print("기본 성능 : ",c4.car_name,c4.color,c4.door,c4.length,c4.width,c4.speed)


# 생성자를 사용한 객체 = 인스턴스 선언
c1 = Car("드뉴아반떼","white",5,2000,1000,60) 
print("철수 성능 : ",c1.car_name,c1.color,c1.door,c1.length,c1.width,c1.speed)

c2 = Car("드뉴아반떼","green",5,2000,1000,100)
print("영희 성능 : ",c2.car_name,c2.color,c2.door,c2.length,c2.width,c2.speed)

c3 = Car("디올뉴그랜저","화이트펄",5,2500,1400,150)
print("반장 성능 : ",c3.car_name,c3.color,c3.door,c3.length,c3.width,c3.speed)




# 기본생성자를 사용한 객체선언
# c1 = Car()
# c1.car_name = "드뉴아반떼"
# c1.color = "white"
# c1.door = 5
# c1.length = 2000
# c1.width = 1000
# c1.up_speed(60) # 현재 speed 60을 더해 줌
# c1.up_speed(40) # 현재 speed는 얼마? 100
# c1.up_speed(50) # 현재 speed는 얼마? 150
# c1.speed = 50   # 현재 speed는 얼마? 50

# c2 = Car()
# c2.car_name = "드뉴아반떼"
# c2.color = "green"
# c2.door = 5
# c2.length = 2000
# c2.width = 1000
# c2.up_speed(100) # 현재 speed 60을 더해 줌

# c3 = Car()
# c3.car_name = "디올뉴그랜저"
# c3.color = "화이트펄"
# c3.door = 5
# c3.length = 2500
# c3.width = 1400
# c3.up_speed(150) # 현재 speed 60을 더해 줌

# print("철수 성능 : ",c1.car_name,c1.color,c1.door,c1.length,c1.width,c1.speed)
# print("영희 성능 : ",c2.car_name,c2.color,c2.door,c2.length,c2.width,c2.speed)
# print("반장 성능 : ",c3.car_name,c3.color,c3.door,c3.length,c3.width,c3.speed)

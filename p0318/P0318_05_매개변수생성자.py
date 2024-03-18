class Tv: #클래스선언 - 설계도
    channel = 0
    color = "black"
    size = 65
    volume = 0

    def __init__(self,color="",size=0,volume=0,channel=0):
        self.color = color
        self.size = size
        self.volume = volume
        self.channel = channel
    
    def up_volume(self,volume):
        self.volume += volume
    def down_volume(self,volume):
        self.volume -= volume
        
    def up_channel(self,channel):
        self.channel += channel
    def down_channel(self,channel):
        self.channel -= channel            
   
    
# 철수-화이트,채널 10변경,2증가 
t1 = Tv() #객체선언 - 제품생산
t1.color = "화이트"
t1.size = 65
t1.volume = 0
t1.channel = 10
t1.up_channel(2)
print(f"철수 TV : {t1.color}, {t1.size}, {t1.volume}, {t1.channel}")

# 영희-핑크,채널 7, 채널 5증가
t2 = Tv("핑크",65,0,7)
print(f"영희 TV : {t2.color}, {t2.size}, {t2.volume}, {t2.channel}")
t2.up_channel(5)
print(f"영희 TV : {t2.color}, {t2.size}, {t2.volume}, {t2.channel}")

# 반장-실버,채널 1, 채널 3증가
t3 = Tv("실버",65,0,1)
print(f"반장 TV : {t3.color}, {t3.size}, {t3.volume}, {t3.channel}")
t3.up_channel(3)
print(f"반장 TV : {t3.color}, {t3.size}, {t3.volume}, {t3.channel}")

    
    
    
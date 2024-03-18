class lotto:
    number = 0
    shape = "circle"
    
    def __init__(self,number):
        self.number = number
        

# lotto 1-45까지의 숫자를 입력한 리스트를 생성한 후, 출력하시오.

l_list = []

for i in range(45):
    l = lotto(i+1)
    l_list.append(l)

for i in range(45):
    l = l_list[i]   
    print("로또 번호 : ",l.number)  
        
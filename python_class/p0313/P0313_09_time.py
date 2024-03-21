import time
import random

for i in range(1,100+1):
    if i%10 == 0:
    #    time.sleep(3) 
       num = random.randint(1,5)
       print(num,"초 대기")
       time.sleep(num)
       pass
    print(i)
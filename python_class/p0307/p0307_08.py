import random

fruit = { 'peach':'복숭아','orange':'오렌지','apple':'사과',
         'pear':'배','grapes':'포도','mango':'망고','kiwi':'키위'}

f_list = list(fruit.keys())
print(f_list)

f_list_ran = random.sample(f_list,4)
print("랜덤추출 : ",end=" : ")
for f in f_list_ran:
    print(fruit[f],end=",")
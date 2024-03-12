import random

fruit = { 'peach':'복숭아','orange':'오렌지','apple':'사과',
         'pear':'배','grapes':'포도','mango':'망고','kiwi':'키위'}

print("개수: ",len(fruit))
# 랜덤으로 4개를 출력 - 랜덤으로 4개를 추출
# 랜덤은 리스트
# key를 리스트 타입으로 변경
print(fruit.keys()) # 딕셔너리에서 key값 추출

f_list = random.sample(list(fruit.keys()),4)

f_list2 = ["kiwi","grapes","peach","pear"]

print(fruit[f_list2[0]])
print(fruit[f_list2[1]])
print(fruit[f_list2[2]])
print(fruit[f_list2[3]])




# value값을 전체 출력
# for key in fruit:
#     print(fruit[key])
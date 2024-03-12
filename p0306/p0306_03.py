import operator
# numbers에 있는 숫자들이 몇번 나왔는지 
# 딕셔너리로 출력하시오.
numbers = [1,2,4,6,4,3,6,7,1,3,4,3,4,7,7,7,7,1,1,1,7]

counter = {}
for n in numbers:
    if n not in counter:
        counter[n] = 0
    counter[n] += 1

print(counter)        
print(sorted(counter.items(),key=operator.itemgetter(0)))

arrays = ["F", "D", "A", "C", "A", "C", "F", "B", "C", "E", "C", "C", "F", "A", "B", "E", "F", "E"]

a_dic = {}

for array in arrays:
    if array not in a_dic:
        a_dic[array] = 0
    a_dic[array] += 1
    
print(a_dic)        
    



a = [1,2,3,4,5]
b = a #얕은 복사
c = [*a] #전개연산자
# a의 데이터 값을 변경
a[1] = 20
print(b) #변경이 됨
print(c) #변경이 안됨

product =["새우깡","90g",1200,3]

print("상품 : {},무게 : {},가격 : {}원, 유통기한 : {}년".format(
    product[0],product[1],product[2],product[3]))

print("상품 : {},무게 : {},가격 : {}원, 유통기한 : {}년".format
      (*product))


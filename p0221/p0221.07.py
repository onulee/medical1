print(200+100)
print(200-100)
print(200*100) 
print(200/100)

# 해보세요
# 1) 200->50으로 바꿔서 출력해보세요
print(50+100)
print(50-100)
print(50*100) 
print(50/100)
# 2) 100 -> 10 
print(50+10)
print(50-10)
print(50*10) 
print(50/10)
# 일일히 다 써야하는 귀찮음이 있기 때문에 변수를 사용하는 것이다.

# 변수를 사용
# 100 -> 1000 , 10 -> 5
a = 1000
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print('*'*20)
# 함수를 사용하여 사칙연산 계산
def cal(a,b):
    print(a*b)
    print(a/b)
    
cal(100,5)
print('-'*20)
cal(50,2)

num1 = 10
num2  = 5
print(str(num1)+'+'+str(num2)+'='+str(num1+num2))
print(num1,'+',num2,'=',num1+num2)
print('%d+%d=%d'%(num1,num2,num1+num2))
print('{}+{}={}'.format(num1,num2,num1+num2)) 

# 수식을 10 - 5 = 5로 출력하기.
print(str(num1),'-',str(num2),'=',str(num1-num2))
print(str(num1)+'-'+str(num2)+'='+str(num1-num2))
print(num1,'-',num2,'=', num1-num2)
print('%d-%d=%d'%(num1,num2,num1-num2))
print('{}-{}={}'.format(num1,num2,num1-num2))

# 수식을 10 * 5 = 50으로 출력하기
print(str(num1),'*',str(num2),'=',str(num1*num2))
print(num1,'*',num2,'=',num1*num2)
print('%d * %d = %d'%(num1,num2,num1*num2))
print('{} * {} = {}'.format(num1,num2,num1*num2))
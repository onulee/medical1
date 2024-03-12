# 이름을 10번 입력 받으세요
name = []
for i in range(3):
    print('[',str(i+1),']')
    n1 = input('이름을 입력하세요:  ')
    ag = input('나이를 입력하세요:  ')
    p = [n1, ag]
    name.append(p)
print(name)




# 입력 :  이름, 아이디, 비밀번호 (input)
# 5명을 입력 받아서 member 리스트를 만드세요

member = [] # [[홍길동, aaa,1111],[유관순, bbb, 2222]]
for i in range(2):
    print('[',str(i+1),']')
    name = input('이름:  ')
    uid = input('ID:  ')
    upw = input('PW:  ')
    mem = [name, uid, upw]
    member.append(mem)
print('-'*40)
print("[ Member list ]")
print('이름\t아이디\t비밀번호')
for m in range(len(member)):
    print('{}\t{}\t{}'.format(member[m][0],member[m][1],member[m][2]))
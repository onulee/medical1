# list
# 데이터를 잘 관리하기 위해서 묶어서 관리하는 자료형
# 리스트 변수명 = [요소1, 요소2, 요소3 ...]
list1 = []
list2 = [0,2,4]
list3 = ['짝수', '홀수']
list4 = ['홍길동', 100, 100, 100]
list5 = ['짝수', [2,4,6], '홀수', [1,3,5]]
# list 자체도 하나의 요소로 사용가능

# 인덱싱 (index) 리스트를 검색, 접근
# index는 0부터 시작
numL = [0,1,2,3,4]
#       0 1 2 3 4
#      -5-4-3-2-1
# 0을 출력
print(numL[0])
print(numL[-5])
# 인덱스의 범위를 넘어가면 오류출력 numL[10]

# 인덱스를 가지고 리스트의 특정 요소의 값을 수정할 수 있다.
# 리스트명[n] = 값
numL[0] = 20
print(numL) # numL = [20,1,2,3,4]
numL[-1] =  222
print(numL) #numL = [20,1,2,3,222]

# list5 = ['짝수', [2,4,6], '홀수', [1,3,5]]
# 숫자2에 접근하기 위해서는?
print(list5[1]) # [2,4,6]
print(list5[1][0])
# 숫자 5에 접근
print(list5[3][2])
print(list5[-1])
print(list5[3])
print(list5[-1][-1])

# 리스트 슬라이싱: 리스트 자르기
# 콜론 :을 사용해서 ~부터 ~까지
# 리스트명[시작인덱스 : 끝인덱스+1]
# numL = [0,1,2,3,4]
print(numL[2:4]) # 2 이상 4 미만
print(numL[1:]) # 1번 인덱스부터 끝까지
print(numL[:3]) # 처음부터 3번 미만까지 (2번 index까지)
print(numL[:]) # 처음부터 끝까지
print(numL[1:-1]) # 1번부터 끝 바로 앞까지

# 리스트의 길이 : len(리스트명)
print(len(list1))
print(len(list2))
print(len(list3))
print(len(numL))

# 특정요소 삭제: del(리스트명[n])
aa = [100,200,300,400,500,600,700]
print(aa)
del(aa[1])
print(aa) # [100,300,400,500,600,700]
del(aa[3:5])
print(aa) # [100,300,400,700]

# 리스트 값 추가: 리스트명.append(값)
aa = [100,200,300,400,500,600,700]
print(aa)
aa.append(800)
print(aa)
aa.append('숫자')
print(aa)
aa.append([1,2,3])
print(aa)

# 리스트에서 특정값 제거
# 리스트명.remove(값)
aa.remove(200)
print(aa)

aa.append(100)
aa.append(400)
aa.append(100)
print(aa)
# [ 100,300,400,500,600,700,800,'숫자',[1,2,3],100,400,100]
aa.remove(100) # 같은 값이 2개 이상
print(aa)

# aa.remove(1) # 1은 존재하지 않기 때문에 오류출력

# 요소확인 : 내부 포함된 요소의 존재를 확인하는 방법
# in, not in
print(100 in aa)
print(200 not in aa)
print(2 in aa)

f = ['사과', '딸기', '복숭아', '수박', '배']
print('딸기' in f)
 
if '사과' in f:
    print('사과가 있습니다.')
else:
    print('사과가 없습니다.')
    

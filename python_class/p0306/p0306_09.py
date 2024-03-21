students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}, 
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67}, 
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67}, 
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}, 
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
    ]

# 모든 학생의 국어점수를 출력하시오.
for i,s_dic in enumerate(students):
    # print(i,".",s_dic["name"],":",s_dic["kor"])
    print("{}.{} : {}".format(i,s_dic["name"],s_dic["kor"]))
'''
[ 국어 점수 ]
0. 홍길동 : 100
1. 유관순 : 98
2. 이순신 : 88
3.
4.

'''
# 모든 학생의 이름을 출력하시오.
# 0.홍길동 1.유관순 2.이순신 3.김구 4.강감찬
# for i,s_dic in enumerate(students):
#     print("{}.{}".format(i,s_dic["name"]),end=" ")



# print(students[1]['name'])
# print(students[4]['name'])

# # 김구 국어+영어점수 합계를 출력하시오.

# # 이순신 국어점수 100으로 수정하시오.

# 파일 읽어오기

# 1. 파일 열기
# read() : 모든 문자열을 가져옴.
# readline() : 1줄씩 가져옴.
# readlines() : 1줄씩 리스트 타입에 입력해서 모두 가져옴.
# 3. 파일 닫기

# 파일 확인
import os
if os.path.exists("str1.txt"): # 파일존재 확인
    # f = open("str.txt","r",encoding="utf8")
    with open("str.txt","r",encoding="utf8") as f: #변수명을 뒤에 씀.
        txt_list = f.readlines()
        
        for txt in txt_list:
            print(txt,end="")
        print()    
    # f.close() 생략가능   
else:
    print("파일이 존재하지 않습니다.")     



# # readlines # 1줄씩 리스트타입으로 가져옴
# f = open("str.txt","r",encoding="utf8")
# # 1줄씩 리스트타입으로 저장
# txt_list = f.readlines()
# print(txt_list)
# print(txt_list[0])
# f.close() # 파일종료를 반드시 해야 함.

# readline 1줄을 str타입으로 가져옴.
# f = open("str.txt","r",encoding="utf8")
# while True:
#     txt = f.readline()
#     if txt == "": break
    
#     print(txt,end="")

        
    
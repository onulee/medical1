# 파일열기
file = open("memo.txt","w",encoding="utf-8")
    
# 파일 쓰기

print("[ 학생성적입력 ]")
print("-"*40)
while True:
    txt = input()
    if txt == "0":
        print("학생성적을 저장합니다.")
        break
    print(txt)
    file.write(txt+"\n")


# for i in range(10):
#     file.write(f"안녕하세요. {i+1}\n")

# 파일닫기
file.close()

print("파일이 저장되었습니다.")


# print("[ 메모장 실행 ]")
# print("-"*40)
# while True:
#     txt = input()
#     if txt == "0":
#         print("메모장을 저장합니다.")
#         break
#     print(txt)
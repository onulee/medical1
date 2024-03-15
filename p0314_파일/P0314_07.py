# str.txt 파일의 내용을 모두 출력하시오.
# 읽어와서 출력

# 파일열기
f = open("str.txt","r",encoding="utf8")
# 파일읽기
while True:
    content = f.readline()
    if content.strip() == "": break # 빈공백enter키 삭제
    print(content,end="")
# 파일닫기
f.close()

print("-"*50)

# str.txt 파일 내용을 읽어와서
# str1.txt에 그 내용을 추가하시오.

f = open("str.txt","r",encoding="utf8")
ff = open("str1.txt","a",encoding="utf8")

while True:
    content = f.readline()  # 파일내용을 읽어오기
    if content.strip() == "": break
    ff.write(content)       # 파일내용을 추가하기
    
f.close()
ff.close() 

fff = open("str1.txt","r",encoding="utf8")
while True:
    content = fff.readline()
    if content.strip() == "": break
    print(content,end="") 
fff.close()      

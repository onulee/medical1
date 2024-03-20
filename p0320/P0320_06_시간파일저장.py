import datetime

now = datetime.datetime.now()
print(now.month) #03 -> 3
print(now.day)   #20 -> 2
print(now.strftime("%m%d")) #0320

# input 입력받은 데이터를
# p_0320.txt 파일을 생성해서 저장하시오.
# p_0320은 현재날짜를 사용하시오.

str1 = input("글자를 입력하세요.")

fileName = "p_"+ now.strftime("%m%d") + ".txt"
# p_0320.txt
with open(fileName,"w",encoding="utf8") as f:
    f.write(str1+"\n")


import P0315_02

member = P0315_02.idpw()
print(member)

# 파일열기
f = open ("mem.txt","w",encoding="utf8")

# 파일쓰기
for m in member:
    f.write("{},{}\n".format(m[0],m[1]))

# f.write("aaa,1111\n")
# f.write("bbb,2222\n")
# f.write("ccc,3333\n")

# 파일닫기
f.close()

print("파일이 저장되었습니다.")
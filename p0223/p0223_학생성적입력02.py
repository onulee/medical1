print('-'*35)
print('[ 학생성적프로그램 ]')
print('-'*35)
print('1. 학생성적입력')
print('4. 학생성적전체출력')
print('0. 프로그램 종료')
print('-'*35)
choice = int(input('원하는 서비스 번호를 입력하세요:  '))

stu1 =[1,"홍길동",100,100,100,300.0,100.0,1]
stu2 =[2,"유관순",90,85,100,275.0,91.7,2]

if choice == 1:
    print(" [학생성적입력]을 선택하셨습니다.")
    print('-'*18)
    print("[ 학생 성적 입력 ]")
    print('-'*18)
    name = input("이름:  ")
    kor = int(input("국어 성적:  "))
    eng = int(input("영어 성적:  "))
    math = int(input("수학 성적:  "))
    total = (kor+eng+math)
    avg = (total/3)
    rank = int(input("등수 입력:  "))
    stu3 =[1,name,kor,eng,math,total,avg,rank]
    if name == "홍길동":
        print(stu1)
    elif name == "유관순":
        print(stu2)
    else:
        print("조회된 기록이 없습니다.")
    print('-'*35)
elif choice == 4:
    print(" [학생성적전체출력]을 선택하셨습니다.")
    print('-'*18) 
    name1 = input("이름:  ")
    if name1 == "홍길동":
        print('[ 학생 성적 전체 출력 ]')
        print('-'*35)
        print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(stu1[0],stu1[1],stu1[2],stu1[3],stu1[4],stu1[5],stu1[6],stu1[7]))
    elif name1 == "유관순":
        print('[ 학생 성적 전체 출력 ]')
        print('-'*18)
        print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(stu2[0],stu2[1],stu2[2],stu2[3],stu2[4],stu2[5],stu2[6],stu2[7]))
    else:
        print("조회된 기록이 없습니다. 다시 입력해주세요")
elif choice == 0:
    print("[ 프로그램 종료 ]")
    print('-'*35)
else:
    print("선택된 서비스가 없습니다. 다시 입력해주세요.")
        
    
    
    
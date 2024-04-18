import random
words = [ {},
    { "airplane":"비행기","apple":"사과","bakery":"빵집",
      "banana":"바나나","bank":"은행","bean":"콩",
      "bicycle":"자전거","boat":"보트","bowl":"그릇","bus":"버스"},
    { "run" : "달리다","walk" : "걷다","sit" : "앉다",
      "stand" : "서다","sleep" : "자다","read" : "읽다",
      "look" : "보다","do" : "하다","feel" : "느끼다","go" : "가다"},
    { "accumulated":"누적된","additional":"추가적인","adequate":"적당한",
    "administrative":"관리의","affordable":"알맞은","alternative":"대체 가능한",
    "annual":"해마다의","different":"다른","local":"지역의","social":"사회의"}
]

w_title = ["","명사","동사","형용사"]

# 함수선언
def w_quiz(choice):
    print("{}를 선택하셨습니다.".format(w_title[choice]))
    chk = input("퀴즈가 나갑니다. 준비되셨나요?(1.실행, 0.취소)")
    if chk == "1":
        # 1. words[choice] 에서 key값을 추출
        # 2. list타입으로 변경
        w_list = list(words[choice].keys()) #리스트 타입
        # 3. random함수를 써서, 5개 list추출
        ran_list = random.sample(w_list,5)
        
        # 4. 5개 list를 퀴즈에 넣으면 됨.
        
        count = 0
        # for key in words[choice]: #{딕셔너리} -> key
        for key in ran_list: #{딕셔너리} -> key
            # print(key,":",w_noun[key])
            answer = input("{} 단어의 뜻은?".format(key))
            if answer == words[choice][key]:
                print("정답입니다.")
                count += 1
            else:
                print("오답입니다. 정답 : {}".format(words[choice][key]))    
        print("정답개수 : {}, 오답 : {} ".format(count,len(ran_list)-count))
    else:
        print("퀴즈를 취소하셨습니다. 메뉴로 돌아갑니다.") 


while True:
    print("[ 영단어 맞추기 프로그램 ]")
    print("-"*40)
    print("1. 명사")
    print("2. 동사")
    print("3. 형용사")
    print("0. 종료")
    print("-"*40)
    choice = int(input("원하는 번호를 입력하세요.>> ")) # 정수형으로 받음.

    if choice == 1:
        w_quiz(choice)    
    elif choice == 2:
        w_quiz(choice)     
    elif choice == 3:
        w_quiz(choice)
    else:
        print("프로그램을 종료합니다.")
        break
            
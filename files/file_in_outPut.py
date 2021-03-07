# 파일 입출력
# "w" : 파일을 write 쓰기 용도로 열기
# 이미 존재하는 파일에 "w"로 open하면 덮어쓰기가 된다.
# encoding="utf8" 을 입력하지 않으면 한글이 깨질 수 있다.
# open() 파일을 열어주면 필히 close()로 파일을 닫아주어야 한다. 


# --------- 방법1 시작------------
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 40", file=score_file)
# score_file.close()
# --------- 방법1 끝------------

# "a" : 파일을 덮어쓰지 않고 이어서 쓰고 싶을 때 
# "a" 로 txt를 이어서 작성할 때는 print가 아닌 파일명.write() 사용
# 변수명.write()의 경우 print가 아니기 때문에 줄바꿈이 되지 않는다.
# 줄바꿈을 명시적으로 써준다.
# 파일은 꼭 닫아준다.
# --------- 방법2 시작------------
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80") 
score_file.write("\n코딩 : 100")
score_file.close()



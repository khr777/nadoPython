# 파일 입출력(읽기)
# "r" : Read
# read() : 파일의 모든 내용을 읽어온다.
# 읽기 또한 파일을 close() 해준다.
# ---------- 방법 1 시작 ---------
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()
# ---------- 방법 1 끝 ---------






# 파일의 모든 내용이 아닌
# '한줄 한줄' 읽어와서 무언가를 처리하고 싶을 때
# 파일은 역시 open()하고 close()해준다.
# 줄바꿈 안하고 공백으로 출력하고 싶다면 end="" 사용
# -------- 방법 2 시작 ---------
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="") 
print(score_file.readline(), end="") 
print(score_file.readline(), end="") 
score_file.close()
# -------- 방법 2 끝 ---------





# 몇줄인지 모르는 파일을 읽으려 할 때
# -------- 방법 3 시작 ---------
score_file = open("score.txt", "r", encoding="utf8")
while True: # 무한루프
    line = score_file.readline()
    if not line:
        break     # not line : line이 존재하지 않는다면 break로 반복문을 탈출.
    print(line)
    # print(line, end="")
score_file.close()
# -------- 방법 3 끝 ---------






# 값을 리스트에 담아서 처리할 수도 있다.
# -------- 방법 4 시작 ---------
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장 
for line in lines:
    # print(line)
    print(line, end="")
score_file.close()    
# -------- 방법 4 끝 ---------






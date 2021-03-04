# continue 와 break
# 반복문 내에서 사용 가능

# 교실에서 학생 번호를 호명하면 책을 읽게 하는 프로그램
absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡했음

# continue : 아래 코드를 실행하지 말고 다음 반복문으로 실행하라.
# break : 반복문을 바로 탈출해버린다.
for student in range(1, 11): # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    if  student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}은 교무실로 따라와.".format(student))
        break
    print("{0} 번, 책을 읽어보세요.".format(student))

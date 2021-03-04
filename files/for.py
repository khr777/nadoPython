# for (반복문)
# 식당에서 대기번호 부여

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

for waiting_no in [10, 20, 30, 40, 50]:
    print("대기번호 : {0}".format(waiting_no))

# 내가 응용
for waiting_no in range(1, 11): # 1 부터 10 까지 
    print("대기번호 : {0}".format(waiting_no))
    
# randrange()
for wating_no2 in range(5): # 0부터 4까지 
    print("대기번호 : {}".format(wating_no2))
    
# 다른 예제 
starbucks = ["아이언맨", "토르", "아이엠 그루트"]    
for customer in starbucks:
    print("{0}님, 커피가 준비되었습니다.".format(customer))



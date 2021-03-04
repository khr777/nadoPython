# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2 분


# ---------------------- 실패.... 난리다 난리.... ------------------------
# from random import *
# customers = range(1, 51)
# minutes = list(range(5, 51))
# shuffle(minutes)
# total = 0

# setting = {}

# for minute in minutes:
#     setting[minute-5] = minute

# for customer in setting:
#     if 5 <= customer.key <= 15:
#         print("[O] {0}번째 손님 (소요시간 : {1}분".format(customer.key, customer.value))
#         total += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분".format(customer, minute))
# print("총 탑승 승객 : {0} 분".format(total))   


      
# print("총 탑승 승객 : {0} 분".format(total))                    
# for customer in customers:
#     for minute in minutes:
#         if 5 <= minute <= 15:
#             print("[O] {0}번째 손님 (소요시간 : {1}분".format(customer, minute))
#             total += 1
#         else:
#             print("[ ] {0}번째 손님 (소요시간 : {1}분".format(customer, minute))
# print("총 탑승 승객 : {0} 분".format(total))            

# ------------------------------------
# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2 분



# ----------------- 풀이 시작 ------------------------

from random import *
cnt = 0
for i in range(1, 51):
    temp = randrange(5, 51)
    if 5 <= temp <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, temp))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, temp))
print("총 탑승 승객 : {0} 분".format(cnt))        
        
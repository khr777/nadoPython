# 슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지 (0, 1) 값만 가져온다.
print("월 : " + jumin[2:4]) # 2 부터 4 직전까지 (2, 3) 값만 가져온다.
print("일 : " + jumin[4:6]) # 4 부터 6 직전까지 (4, 5) 값만 가져온다.

# 주민번호 앞 6자리 출력
print("생년월일 : " + jumin[0:6]) # 0 부터 6 직전까지 (0 ~ 5) 값만 가져온다.
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지 // 콜론(:)만 입력해도 처음부터 출력할 수 있다. 

# 주민번호 뒤 7자리 출력
print("뒤 7자리 : " + jumin[7:14]) # 7 부터 14 직전까지 (7 ~ 13) 값만 가져온다.
print("뒤 7자리 : " + jumin[7:]) # 7부터 맨 끝까지 // 콜론(:)만 입력해도 마지막까지 출력할 수 있다.

# 주민번호 뒤 7자리 (뒤에부터)
# 맨 뒤에서 7번째부터 끝까지
print("주민번호 뒤 7자리 (뒤에부터) : " + jumin[-7:]) 

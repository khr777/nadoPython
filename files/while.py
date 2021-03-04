# while 반복문

# 스타벅스에서 손님을 5번 불렀는데 나타나지 않으면 커피를 버리는 정책을 만들었다고 가정.
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1  
    if index == 0:
        print("커피는 폐기처분 되었습니다.")
        
# 출력 
# 토르, 커피가 준비 되었습니다. 5 번 남았어요.
# 토르, 커피가 준비 되었습니다. 4 번 남았어요.
# 토르, 커피가 준비 되었습니다. 3 번 남았어요.
# 토르, 커피가 준비 되었습니다. 2 번 남았어요.
# 토르, 커피가 준비 되었습니다. 1 번 남았어요.
# 커피는 폐기처분 되었습니다.        

# 다른 커피숍
customer = "아이언맨"
person = "UnKnown"

while customer != person:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")
    if customer == person:
        print("커피 지급이 완료되었습니다.")
 
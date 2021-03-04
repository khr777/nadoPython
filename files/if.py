# if 

# weather = "맑음"
weather = input("오늘 날씨는 어때요? ") # input() : 사용자의 입력을 받는다.
if weather == "비" or "눈":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물 필요 없어요.")    
    

# 내가 만든 연습문제 
age = int(input("당신의 나이는? "))    
if age <= 8:
    print("당신은 영유아 입니다.")
elif ((age > 8) & (age <= 19)):
    print("당신은 청소년 입니다.")
else:
    print("당신은 성인입니다.")    
    
    
# int() :  정수화
temp = int(input("기온은 어때요? "))    
if 30 <= temp:
    print("너무 더워요. 나가지 마세요.")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요.")    
elif 0 <= temp < 10:
    print("외투를 챙기세요.")    
else:
    print("너무 추워요. 나가지 마세요.")
    
        
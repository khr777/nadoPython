# 표준 입출력
# sep="" 활용법
print("Java", "Python", "JavaScript", sep=" VS ")

# end=" " // 줄바꿈 되지 않고 이어서 출력된다.
print("안녕하세요. 저는", end=" ")
print("홍길동 입니다.")

print("Java", "Python", sep=", ", end="? ")
print("무엇이 더 재미있을까요?")

import sys
print("Python", "Java", file=sys.stdout) # 표준 출력
print("Python", "Java", file=sys.stderr) # error log를 남기기 위함


# 시험 성적
# ljust(칸 수) : 왼쪽 정렬
# rjust(칸 수) : 오른쪽 정렬
# ljust() / rjust() 모두 string 이어야 사용 가능
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")
# 출력
# 수학      :   0
# 영어      :  50
# 코딩      : 100
    
    
# 은행 대기순번표
# 001, 002, 003, ...
# zfill(자리수) : 0으로 채우는 함수 
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))
    
# input() 함수(사용자의 입력을 받은 값은 모두 문자열 저장)의 값은 모두 str (숫자를 입력해도 str) 
# 숫자를 str로 형변환 할 필요가 없다.
answer = input("아무 값이나 입력하세요 : ") 
print(type(answer))
# print("입력하신 값은 " + answer + " 입니다.")
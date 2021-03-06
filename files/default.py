# 기본값

# 코드 줄바꿈을 할 때는 \ 입력하고 enter해서 이어서 쓰면 된다.

# -------- 아래 코드를 실행하기 위한 주석처리 ---------
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
#         .format(name, age, main_lang))
    
# profile("유재석", 30, "파이썬")    
# profile("김태호", 20, "자바")    





# 같은 나이라면 나이, 주 언어(수업)를 하나하나 입력해줄 필요가 없다.
# 같은 학교 같은 학년 같은 반 같은 수업.
# 기본값 : 위와 같은 경우에 사용하는 것이 기본값.
def profile(name, age=17, main_lang="파이썬"):  # <- 기본값 설정하는 방법
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
        .format(name, age, main_lang))
    
profile("유재석")
profile("김태호")
    
    
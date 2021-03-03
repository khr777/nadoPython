# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오. 

# 예) http://naver.com 
# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                (nav)                  (5)             (1)       (!)
# 예) 생성된 비밀번호 : nav51! 

# 방법 1
# strUrl = "http://kakao.com"   kak50!
# strUrl = "http://google.com"  goo61!      
strUrl = "http://daum.net"     # nav51!
domain = strUrl[7:] # naver.com
index = domain.index(".") # 5
hint = domain[:index] # naver
pw1 = hint[0:3] # nav 
pw2 = len(hint) # 5 
pw3 = hint.count("e")
print(f"생성된 비밀번호 : {pw1}{pw2}{pw3}!")

# 방법 2
url = "http://daum.net"
my_str = url.replace("http://", "")  # 규칙 1
my_str = my_str[:my_str.index(".")] # 규칙 2
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))

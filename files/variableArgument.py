# '가변 인자'를 이용한 함수 호출

# 끝에 end=" " 이렇게 입력해주면 다음 출력이 줄바꿈 되지 않고 이어서 출력된다. 

# 방법1
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") 
#     print(lang1, lang2, lang3, lang4, lang5)

# lang1,2,3,4,5 -> *language 로 수정 
def profile(name, age, *language): # 가변 인자
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") 
    for lang in language:
        print(lang, end=" ")
    print() # 마지막에 줄바꿈을 해주기 위한 용도.
    
profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")    
profile("김태호", 25, "Kotlin", "Swift")
# 위와 같이 ""을 써주어도 되나, 비효율적이다.
# 사용 가능한 언어가 5개보다 많아질 수도 있다. -> 방법1의 경우 함수 자체를 수정해주어야 한다. 번거롭다.



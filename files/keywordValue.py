# 키워드 값

def profile(name, age, main_lang):
    print(name, age, main_lang)
    
# 매개변수 위치가 달라도 key=value로 입력해주면 매개변수가 알아서 잘 찾는다.    
profile(age=30, name="김태호", main_lang="Java")    
profile(main_lang="Python", age=10, name="유재석")
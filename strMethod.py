# 문자열
python = "Python is Amazing"
print(python)

# lower() 함수 : 모두 소문자로 출력 
print(python.lower())

# upper() 함수 : 모두 대문자로 출력
print(python.upper())

# isupper() / islower() : 해당 index의 대/소문자를 참/거짓으로 확인하는 함수 
print(python[0].isupper()) # True
print(python[0].islower()) # False 


# len() : 문자열 길이 구하는 함수 
length = len(python)
print(length)


# replace("", "") : 특정 문자를 원하는 문자로 치환
print(python.replace("Python", "Java"))

# index() : 특정 문자의 index를 확인하는 함수
# 제일 첫번째에 있는 특정 문자의 index를 찾는다(특장 문자 중복의 경우)
index = python.index("n")
print(index)

# 첫번째 특정 문자 이후의 중복 문자 index를 반환
index = python.index("n", index + 1)
print(index)

# find() : index() 함수와 마찬가지로 특정 문자열의 index를 계산해준다.
print(python.find("n")) # 5

# find() 에서는 원하는 값이 없을 때 -1을 반환한다.
print(python.find("Java")) # -1

# index()에서는 원하는 값이 없으면 Compile error가 발생한다.
# print(python.index("Java")) # compile error 

# count() : 특정 문자가 몇번 등장하는지 반환
print(python.count("n"))


# 사전 (key : value)
cabinet = {3:"유재석", 100:"김태호"}

# value 출력 방법 1.
print(cabinet[3]) # [key 입력] -> value 출력    
print(cabinet[100])# 리스트 [] : 순서를 가지는 객체의 집합 

# value 출력 방법 2.
print(cabinet.get(3)) 
print(cabinet.get(100))

# 없는 key에 대해 []로 출력하면 error 
# print(cabinet[5])   error 발생 -> 프로그램 종료된다. 

# 없는 key에 대해 .get() 함수로 호출하면 'None' 출력
print(cabinet.get(5))   # None 출력 

# .get(key)가 없다면 기본 출력 지정 가능
print(cabinet.get(5, "프로그램 계속 실행")) # 5 라는 key는 쓸 수 있다는 의미.

# 사전 안에 key가 있는지 확인하는 방법
print(3 in cabinet) # True
print(234 in cabinet) # False

# 정수가 아닌 '문자열'로 key 설정 가능
cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"]) # 유재석 출력 
print(cabinet["B-100"]) # 김태호 출력 

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국" # 중복되는 key에 새로운 value를 할당하면 update
cabinet["C-20"] = "조세호" # 새로운 key:value를 할당하면 새로운 값이 저장
print(cabinet)

# 간 손님 / del 사용
# key 삭제 
print(cabinet)
del cabinet["A-3"]
print(cabinet)

# keys() : key 들만 출력 
print(cabinet.keys())

# values() : value 들만 출력
print(cabinet.values())

# items() : key, value 쌍으로 출력
print(cabinet.items())

# clear() : 모든 값을 삭제, 목욕탕 폐점 
cabinet.clear()
print(cabinet)
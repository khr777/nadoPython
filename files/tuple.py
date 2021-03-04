# 튜플 : 리스트와 다르게 내용 변경이나 추가를 할 수 없다. 
# 할 수 있는게 많이 없다. 
# 그러나 속도가 리스트보다 빠르다. 
# '변경되지 않는 목록'을 다룰 때 tuple을 사용한다. 

# tuple 사용시 () 괄호를 사용
# index를 사용해서 값을 출력
menu = ("돈까스", "치즈까스")
print(menu[0])  
print(menu[1])

    
# tuple 형태로 보이지만 변수 값 변경 가능 
(name, age, hobby) = ("김종국", 20, "코딩")    
print(name, age, hobby)
print(name)
print(age, hobby)
name = "어어어어"
print(name) # 어어어어 출력 

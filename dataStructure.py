# 자료구조의 변경 

# 커피숍 

# 집합
menu = {"커피", "우유", "주스"}   
print(menu, type(menu)) # 출력 : {'주스', '커피', '우유'} <class 'set'>

# 리스트 
menu = list(menu)
print(menu, type(menu)) # 출력 : ['주스', '커피', '우유'] <class 'list'>

# 튜플
menu = tuple(menu)
print(menu, type(menu)) # 출력 : ('주스', '커피', '우유') <class 'tuple'>

# 다시 집합 
menu = set(menu)
print(menu, type(menu)) # 출력 : {'우유', '주스', '커피'} <class 'set'>
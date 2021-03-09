# 내장 함수 : 내장되어 있어서 따로 import 할 필요 없이 사용 가능한 함수. 

# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요? ")
# print("{0}은 아주 좋은 언어입니다! ".format(language))


# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
# 출력 : ['__annotations__', '__builtins__', '__cached__', '__doc__', 
# '__file__', '__loader__', '__name__', '__package__', '__spec__']
import random # 외장 함수 
print(dir())
# 출력 : ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', 
# '__loader__', '__name__', '__package__', '__spec__', 'language', 'random']
import pickle
print(dir())
# 출력 : ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', 
# '__loader__', '__name__', '__package__', '__spec__', 'pickle', 'random']


# print(dir(random))
# 출력 : random 모듈에서 사용할 수 있는 변수, 함수 모두를 알려준다.  


lst = [1, 2, 3, 4]
# print(dir(lst))  # 출력 : 리스트에서 쓸 수 있는 내용들이 출력된다.

name = "Jim"
print(dir(name)) # 출력 : name에 대해서 쓸 수 있는 많은 것들을 제공해준다. 


# 위의 것들 말고도 
# 구글에서 list of python builtins 라고 검색 
# Built-in Functions-Python 3.8.1 documentation  클릭 
# 사이트 언어는 좌측 상단에서 변경할 수 있음.
# 파이썬 내에서 사용할 수 있는 내장함수 정보를 알 수 있다.
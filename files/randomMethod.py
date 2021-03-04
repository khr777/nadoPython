# 랜덤 함수 
# '랜덤 라이브러리 모든 것을 사용하겠다.'라는 의미.
from random import *
print(random()) 
# 0.~~~~~   random 함수를 통해서 '난수'를 뽑아낸 것이다.
# 0.0 ~ 1.0 미만의 임의의 값 생성.



print(random() * 10)
# 0.0 ~ 10.0 미만의 임의의 값 생성.


print(int(random() * 10))  
print(int(random() * 10))  
print(int(random() * 10))  
# 0 ~ 10 미만의 임의의 값 생성.
# 소수점이 출력되는게 싫다면.



print(int(random() * 10) + 1)  
print(int(random() * 10) + 1)  
print(int(random() * 10) + 1)  
# 1 ~ 10 이하의 임의의 값 생성.



# 로또 값 출력해보기
# 방법1 : random() // 1 ~ 45까지 임의의 숫자 생성
print("-------------LOTTO-------------random()")
print(int(random() * 45 ) + 1)
print(int(random() * 45 ) + 1)
print(int(random() * 45 ) + 1)
print(int(random() * 45 ) + 1)
print(int(random() * 45 ) + 1)
print(int(random() * 45 ) + 1)



# 방법2 : randrange() // 1 ~ 45까지 임의의 숫자 생성
print("-------------LOTTO-------------randrange()")
print(randrange(1, 46))  # 1부터 46 미만의 임의의 숫자 생성
print(randrange(1, 46)) 
print(randrange(1, 46)) 
print(randrange(1, 46)) 
print(randrange(1, 46)) 
print(randrange(1, 46)) 

# 방법3 : randint(a, b) // a와 b를 포함한 이 둘 사이의 모든 숫자를 return
print("-------------LOTTO-------------randint()")
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
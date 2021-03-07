# 모듈은 쓰려는 같은 경로에 있거나 파이썬 폴더들이 모여있는 폴더 안에서 사용 가능하다.
# theater_module 모듈을 사용하는 방법

# 방법 1
# import theater_module
# theater_module.price(3)  # 3명이서 영화 보러 갔을 때 가격 
# theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
# theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때


# 방법 2
# 모듈의 별칭을 주어 간단하게 활용하는 방법
# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)


# 방법 3 
# from theater_module import * # theater_module의 모든(*)것을 사용하겠다.
# price(3)
# price_morning(4)
# price_soldier(5)

# 방법 4 : from ~ import의 변형 
# from theater_module import price, price_morning # 필요한 것들만 골라서 import 할 수 있다.
# price(8)
# price_morning(10)

# 방법 5 : 모듈의 1개의 기능만 import 하는 경우에도 별칭을 붙일 수 있다.
from theater_module import price_soldier as price
price(10)
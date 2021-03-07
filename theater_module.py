# 모듈 (module) : 필요한 것들 끼리 부품처럼 잘 만들어진 파일이라고 보면 된다.
# 자동차 타이어 마모, 펑크 -> 타이어만 교체
# 자동차 범퍼 고장 -> 범퍼만 교체
# 코드를 부품 교체하듯 부분만 교체하면 유지보수도 쉽고 코드의 재사용성이 수월해진다.
# 파이썬에서는 함수 정의, 클래스 들의 파이썬 정의를 담고 있는 파일을 모듈이라고 한다. 
# 확장자가 .py 이다.

# 영화를 볼 수 있는 극장이 있는데, 희한하게 현금만 받는다. 
# 잔돈을 바꿔주지도 않는다.


# 현재 theater_module.py 파일 자체가 모듈이다.

# 일반 가격
def price(people):
    print("{0}명 가격은 {1:,}원 입니다.".format(people, people * 10000))

# 조조 할인 가격
def price_morning(people):
    print("{0}명 조조 할인 가격은 {1:,}원 입니다.".format(people, people * 6000))

# 군인 할인 가격
def price_soldier(people):
    print("{0}명 군인 할인 가격은 {1:,}원 입니다.".format(people, people * 4000))
    
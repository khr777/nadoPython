# 클래스 만들기 
# __init__ : Python에서 사용되는 생성자
# marine이나 tank 같은 객체가 만들어질 때 자동으로 호출되는 부분.
# 객체 : 클래스에 의해 만들어진.
# marine, tank는 Unit 클래스의 '인스턴스'라고 한다.
# 멤버 변수 : 클래스 내에서 정의된 변수(self.name/self.hp/self.damage)

# ------------ 클래스 생성 시작 --------------
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
# ------------ 클래스 생성 끝 --------------   

     
# 객체를 생성할 때는 'self'를 뺀 나머지의 매개변수 개수와 동일하게 전달해주어야 한다.
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)



# 멤버 변수 예시
# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 ( 빼앗음 )
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True  # clocking이라는 변수는 Unit 클래스에 없지만 추가로 할당한 것.
# 이와 같이 파이썬에서는 클래스 외부에서 변수를 추가 할당해서 사용할 수 있다.
# 하지만 해당 변수는 wraith2에 할당 된 것으로 wraith1은 clocking이라는 변수를 사용할 수 없다.

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))


# 클래스 외부에서 원하는 변수 확장
# 확장된 변수는 확장한 객체에 대해서만 적용되고 
# 다른 객체에 대해서는 적용되지 않는다.

        
        
# 클래스 만들기 
# __init__ : Python에서 사용되는 생성자
# marine이나 tank 같은 객체가 만들어질 때 자동으로 호출되는 부분.
# 객체 : 클래스에 의해 만들어진.
# marine, tank는 Unit 클래스의 '인스턴스'라고 한다.

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
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

        
        
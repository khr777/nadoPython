class Unit:
    def __init__(self):
        print("Unit 생성자")
        
class Flyable:
    def __init__(self):
        print("Flyable 생성자")        
        
class FlyableUnit(Unit, Flyable): # Flyable을 먼저 쓰면 Flyable 생성자가 호출된다.
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)        

# 드랍쉽 : 유닛을 공중으로 태우고만 다니는 로봇, 공격할 수 없음.
dropShip = FlyableUnit() # 출력 : Unit 생성자 / Flyable 생성자는 초기화 되지 않았다.


                
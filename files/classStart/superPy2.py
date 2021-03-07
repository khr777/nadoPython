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

# 결론 : 다중 상속을 받을 경우에는 super() 사용을 권장하지 않는다.
# 명시적으로 init을 통하여 부모 클래스를 호출하도록 한다.        

# 드랍쉽 : 유닛을 공중으로 태우고만 다니는 로봇, 공격할 수 없음.
dropShip = FlyableUnit() # 출력 : Unit 생성자 / Flyable 생성자는 초기화 되지 않았다.


                
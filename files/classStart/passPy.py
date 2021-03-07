# pass 

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")            
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed=0):
        Unit.__init__(self, name, hp, speed) # 부모에게 값을 넘겨주어 초기화하는 작업.
        self.damage = damage            
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]".format(
            self.name, location, self.damage
        ))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
            

# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 X

# 날 수 있는 기능을 가진 클래스 
class Flyable(Unit):
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(
            name, location, self.flying_speed
        ))
        
# 공중 공격 유닛 클래스 // 다중 상속 
class FlyableAttackUnit(Flyable, AttackUnit):
    def __init__(self, name, hp, damage, flying_speed): # 초기화 단계 
        Flyable.__init__(self, flying_speed)
        AttackUnit.__init__(self, name, hp, damage, )
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 뭔가 추가로 더 정의해야 하지만 일단 'pass'로 정의
# pass 의미 : 일단은 넘어간다. 오류없이 넘어간다. pass를 입력하면 일단은 완성된것 처럼 보여진다. 
# pass는 다른 곳에서도 쓸 수 있다.     
    
    
# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛. 8개 유닛을 만든 후 추가로 서플라이 디폿을 만들어야 한다.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시") # 상속 받고 부모 클래스를 호출하지 않았는데도 오류 없음(pass 때문)



# pass를 생성자가 아닌 다른 곳에서 사용하는 예시 
# ---------------- 예시 시작 ---------------
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")    
    
def game_over():
    pass 

game_start()
game_over()  # 오류 없음 (pass를 했기 때문에)   
# ---------------- 예시 끝 ---------------

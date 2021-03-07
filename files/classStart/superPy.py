# super

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed=0):
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
        # Unit.__init__(self, name, hp)
        super().__init__(name, hp) # 위와 같은 부모 클래스 초기화로 super는 ()를 붙이고 self를 보내지 않는다.
        self.location = location

# superPy2.py 참고 (다중상속에서의 문제 발생)
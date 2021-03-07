# 메소드 오버라이딩

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")            
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# 상속받을 때 '클래스명(상속받을 클래스명)'
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
        

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 20, 10)

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음.
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)



# 지상/공중 유닛인지 매번 확인해서 move, fly 함수를 사용해야 한다.
# 번거롭다.
# 해결 방법 : '메소드 오버라이딩'을 통해서 해결할 수 있다.
vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")
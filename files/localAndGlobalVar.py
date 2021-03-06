# 지역변수와 전역변수 

# 지역변수 : 함수 내에서만 사용 가능.
# 함수 호출되면 만들어졌다가 함수 호출이 끝나면 사라지는 변수.

# 전역변수 : 프로그램 모든 공간 어디에서든 불러서 사용할 수 있는 변수.

# 예시 : 군대 
gun = 10

def checkPoint(soldiers):
    global gun # 전역 공간에 있는 gun 사용 
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    
# 일반적으로 전역 변수를 사용하면 코드 관리가 어려워서 권장하진 않는다. (global gun)
# 가급적 함수의 전달 값으로 던져서 반환값을 받아서 사용한다.    
def checkPoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))    
# checkPoint(2) # 2명이 경계 근무 나감
gun = checkPoint_ret(gun, 3)
print("남은 총 : {0}".format(gun))
# 전달값과 반환값

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withDraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance
def withDraw_night(balance, money): # 출금액이 잔액보다 크다는 가정은 일단 제외
    comission = 100 # 수수료 100원
    return comission, balance - money - comission
        

balance = 0 # 잔액
balance = deposit(balance, 1000)
balance = withDraw(balance, 500)
comission, balance = withDraw_night(balance, 200)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(comission, balance))

# finally : 오류가 발생하지 않건, 발생하건 무조건 제일 마지막에 실행되는 부분.
# 오류 발생 여부와 상관없이 무조건 실행되는 finally 를 통해서 
# 우리 프로그램의 완성도를 높일 수 있다.

# Exception을 상속 받는다.
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg
    
# 한자리 숫자에 대해서만 나눗셈을 허용하는 계산기 프로그램.
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력해주세요 : "))
    num2 = int(input("두 번째 숫자를 입력해주세요 : "))
    if num1 >= 10 or num2 >= 10: # 특정 조건에 에러를 발생시켜서 except 부분을 실행시킬 수 있다.
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")    
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")    
    print(err)
finally: 
    print("계산기를 이용해 주셔서 감사합니다.")    

    
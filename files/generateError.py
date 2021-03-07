# 의도적으로 에러 발생시키기.

# 한자리 숫자에 대해서만 나눗셈을 허용하는 계산기 프로그램.
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력해주세요 : "))
    num2 = int(input("두 번째 숫자를 입력해주세요 : "))
    if num1 >= 10 or num2 >= 10: # 특정 조건에 에러를 발생시켜서 except 부분을 실행시킬 수 있다.
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")    
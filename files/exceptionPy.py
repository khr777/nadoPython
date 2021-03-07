# 예외 : 어떤 에러가 발생했을 때, 처리해주는 것.
# 에러 : 실책, 실수, 잘못된 것을 입력했을 때
# 예시) 택새 기사님이 11층 배송지로 이동하는데 그 아파트는 10층까지 밖에 없을 때...등
# URL 잘못 적거나, 숫자를 입력해야 하는데 문자열을 입력했을 때.

# 예시 문제) 나누기 전용 계산기 프로그램.
# 방법 1.
try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력해주세요 : "))
    num2 = int(input("두 번째 숫자를 입력해주세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2))) # 실수 출력하지 않기 위해서 int() 형변환 
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: # 해당하는 error 코드를 그대로 보여준다.  / 출력 : division by zero
    print(err)    
    

# 방법 2.
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력해주세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력해주세요 : ")))
    # nums.append(nums[0] / nums[1])
    print("{0} / {1} = {2}".format(nums[0], nums[1], int(nums[2]))) # 실수 출력하지 않기 위해서 int() 형변환 
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: # 해당하는 error 코드를 그대로 보여준다.  / 출력 : division by zero
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생했습니다.")    
    print(err)    
    
    
# except:            ValueError, ZeroDivisionError를 제외한 나머지 에러에 대해서 모두 처리 가능
#     print("알 수 없는 에러가 발생했습니다.")    

# except IndexError as err:
#     print(err)    
        
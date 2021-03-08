# package : 모듈들을 모아놓은 집합 / 하나의 디렉터리에 여러 모듈 파일들을 갖다놓은 것을 
    
# 신규 여행사 프로젝트를 담당하게 된 (태국, 베트남)

# travel 폴더와 함께 


# travel 패키지 안에 있는 thailand 모듈에 대한 thailand 패키지 클래스를 직접 사용해보는 것.
# 주의할 점 : import를 할 때는, 패키지와 모듈명만 입력 가능(클래스나 함수명을 입력할 수 없다.)
import travel.thailand 

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()


# from ~ import를 할 때는 클래스/함수/패키지/모듈 모두 import 할 수 있다.
# travel 패키지 안에 있는 thailand 모듈에서 ThailandPackage라는 클래스를 import하는 것이다.
# 아래는 '클래스' import한 예제
from travel.thailand import ThailandPackage
trip_to2 = ThailandPackage() # 객체 생성 
trip_to2.detail()

# 모듈을 import 하는 예제
from travel import vietnam
trip_to3 = vietnam.VietnamPackage() # 객체 생성
trip_to3.detail()



# __all__

# from random import * 

from travel import * # 패키지 안에 포함된 것들 중에서 import 되기 원하는 것들만 공개하고 원하지 않는 것은 비공개 할 수 있다.(__init__)
trip_to = vietnam.VietnamPackage() 
# travel 패키지의 모든 것을 사용하겠다고 했지만 vietnam이 없다고 오류 발생한다. 그러나 실행은 잘 된다.
# pylint의 문제를 잠깐 숨기기 위한 방법

# File - preferences - settings - 'linting'이라고 검색 - Python>linting:Enabled 를 체크해제해서 잠시 비활성화 시킨다.

trip_to2 = thailand.ThailandPackage()
trip_to.detail()
trip_to2.detail()

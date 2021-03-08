# 패키지, 모듈 위치 
# 확인하는 법

import inspect
import random
from travel import *

# print(inspect.getfile(random))    # 출력 : C:\Python38\lib\random.py
# print(inspect.getfile(thailand)) # 출력 : c:\Users\kim56\OneDrive\바탕 화면\PythonWorkspace\travel\thailand.py
# 문제가 없는 부분인데 pylint 오류 발생 시킴. 출력도 문제 없이 잘 되고 있음.


# 다음 진행 순서 
# 1. travel 패키지를 C:\Python38\lib\random.py 여기로 옮겨본다.
# 2. 기존 travel 패키지의 이름은 travel_temp라고 변경한다.
# 3. 테스트를 한 후, lib 폴더 안의 travel 폴더는 다시 삭제하고 _temp 폴더 이름도 
# 원래대로 변경.

# 다른 프로젝트를 할 때에도, 모듈을 lib 폴더로 옮겨서 사용할 수 있다.
# 모듈은 같은 경로에 있어야 하기 때문에... 
# 그럼 진짜 lib 폴더에 붙여넣지 않고는 사용할 수가 없는건가?.....
print(inspect.getfile(random)) # 출력 : C:\Python38\lib\random.py
print(inspect.getfile(thailand)) # 출력 : C:\Python38\lib\travel\thailand.py
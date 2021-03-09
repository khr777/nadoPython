# 외장 함수 : 내장함수와는 다르게 import를 해야 사용할 수 있는 함수.

# 구글에서 list of python modules 라고 검색 
# Python Module index - Python 클릭 
# 외장함수 목록을 볼 수 있다.

# glob : 경로 내의 폴더 / 파일 목록 조회 ( 윈도우 dir 와 같은)
import glob
print(glob.glob("*.py")) # py로 끝나는 모든 파일을 검색 (확장자가)

# os : 운영체제에서 제공하는 기본 기능
# 폴더를 만들고 삭제하는 기능 등

import os 
print(os.getcwd()) # 현재 디랙토리 표시

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder) # 폴더 삭제
    print(folder, "폴더를 삭제하였습니다.")
    
else:
    os.makedirs(folder) # 폴더 생성
    print(folder, "폴더를 생성하였습니다.")    
    
print(os.listdir())   # glob 같은


# time : 시간 관련 함수 
import time 
print(time.localtime())
# 출력 : time.struct_time(tm_year=2021, tm_mon=3, tm_mday=9,
# tm_hour=1, tm_min=19, tm_sec=18, tm_wday=1, tm_yday=68, tm_isdst=0)
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 출력 : 2021-03-09 01:20:52


# datetime
import datetime
print("오늘 날짜는 ", datetime.date.today())
# 출력 : 오늘 날짜는  2021-03-09

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은 ", today + td) # 오늘로부터 100 후
# 출력 : 우리가 만난지 100일은  2021-06-17
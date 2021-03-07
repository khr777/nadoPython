# pickle : 프로그램 상에서 우리가 사용하고 있는 데이터를 파일 형태로 저장해주는.
# 파일을 누군가에게 주면 그 분이 파일을 열어서 pickle 이용해서 데이터를 가지고 와서 
# 코드에서 또 사용할 수 있는.
# pickle을 사용하려면 import 해야 한다. 


# 우선 pickle 이라는 module을 import 
# pickle을 이용해서 파일을 쓰고, 불러올 수 있는 유용한 라이브러리.
import pickle 

# ----------------- pickle 파일 작성 시작 ------------------
# 일단 파일에다가 저장을 할 것이다.
# 파일 타입은 pickle이고, "write" 목적이며 b를 붙여준다.
# b : 바이너리 의미.
# pickle을 사용하려면 꼭 바이너리 타입을 정의 해주어야 한다.
# pickle에는 따로 encoding을 설정해줄 필요 없다. 
profile_file = open("profile.pickle", "wb")
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
# pickle을 이용해서 파일에 쓰기 위한 작업
# profile 에 있는 정보를 profile_file 에 pickle을 이용해서
pickle.dump(profile, profile_file)
profile_file.close()
# ----------------- pickle 파일 작성 끝 ------------------


# ----------------- pickle 파일 불러오기 시작 ------------------
# 쓰기가 아닌 읽기이므로 "rb" 입력 
# 뒤에 b를 입력해서 불러올 파일이 바이너리 형태임을 명시적으로 알려준다.    
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile 에 불러오기.
print(profile)
profile_file.close()
# ----------------- pickle 파일 불러오기 끝 ------------------


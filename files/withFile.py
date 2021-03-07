# with : 파일 쓰기, 읽기를 조금 더 수월하게 할 수 있는

# pickle, with를 사용해서 파일 불러오기
# ----------- 방법 1 시작 -------------
import pickle

# with로 파일을 읽어온다.
# as profile_file : 파일을 열어서 profile_file이라는 변수에 저장.
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file)) # 출력 : {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']} 
# with 문을 수행하고 '자동'으로 '종료'가 된다.
# close()를 해줄 필요가 없다. 
# ----------- 방법 1 끝 -------------

# pickle을 사용하지 않고 with만으로 파일 쓰기
# ----------- 방법 2 시작 -------------
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")
# study_file.close() 해줄 필요 없다.    
# ----------- 방법 2 끝 -------------


# pickle을 사용하지 않고 with만으로 파일 불러오기
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
# study_file.close() 해줄 필요 없다.    


    
    


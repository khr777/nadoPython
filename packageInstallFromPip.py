# pip로 패키지 설치하는 방법.
# 이미 수많은 패키지들이 존재하고 있고, 누군가는 새롭게 만들고 있다.
# 파이썬은 이미 만들어진 패키지들을 필요한 곳에 가져가 쓰는 것도 중요한 부분이다.

# 파이썬 패키지 검색 방법
# 구글 -> pypi 검색 -> PyPI . The Python Package Index 접속 
# -> 중간에 projects 갯수 확인 가능 
# Or Browse projects 클릭 해보기 -> Filter by classifier : 다양한 기준으로 찾아볼 수 있다.
# 필요한 패키지가 있는지 미리 검색을 해보고 없는 부분에 대해서는 
# 직접 구현하는게 효율적일 것이다.

# 웹스크래핑으로 아주 유명한 패키지 : beautifulsoup 검색해보기 (PyPI 안에서)
# beautifulsoup4 4.8.2 클릭 -> 설치 명령어 복사 -> 터미널에 입력해서 설치.

# 예제의 3줄 먼저 실행해보기.
# 코드 실행해보기 -> 출력문을 확인해본다.
# 출력되는 코드에 대해서는 아직 알지 않아도 되며, 패키지를 설치해서 제대로 출력이 되는구나.
# 작동이 되는구나, 까지만 알고 넘어가면 된다. 


# pip list 명령어 : 현재 설치된 패키지 내용에 대해서 알 수 있다.
# pip show beautifulsoup4 명령어 : beautifulsoup4에 대한 정보를 알려준다.
# pip install --upgrade beautifulsoup4(패키지명) 명령어 : 업그레이드 된 패키지가 있다면
# 업그레이드를 할 수 있다. 
# pip uninstall beautifulsoup4(패키지명) 명령어 : 내가 설치한 패키지를 삭제하고 싶을 때 



from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
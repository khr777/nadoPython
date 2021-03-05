# 필히 참고 

<br>
<br>


## 기술 스택 익히기

- 기본적으로 : Java
- Unix 콘솔 명령어 
- CLI 명령어
- 파이썬
- django
> 장고는 파이썬으로 작성된 오픈 소스 웹 프레임워크로, 모델-뷰-컨트롤러 패턴을 따르고 있다.
- 웹서버 구축(Python)
- 도스 커맨드 명령어
- 도스 프롬프트(CLI)

<br>
<br>

## F.E
|jQuery|react/react-native|
|--|--|

<br>
<br>

## B.E
|was(와스) : Spring Boot | node.js / Python|
|--|--|

|DB | SQL / MySQL(MariaDB)| 
|--|--|

<br>
<br>

# DevOps
|Infra|
|--|

|Deploy(배포)|
|--|

|Operation|
|--|

<br>
<br>


# etc(기타 등등)

<br>
<br>
<br>

## 자주 사용하는 Service Port
> Protocol 종류

*프로토콜(Protocol)은 컴퓨터나 네트워크 장비가 서로 통신하기 위해 미리 정해 놓은 약속, 규약*
- 컴퓨터, 네트워크 장비마다 사용하는 언어가 다를 수 있어 소통을 할 수 없을 것이기에.

<br>

| Name | Port | Description | TCP/UDP |
|--|--|--|--|
|FTP|20|파일 전송 프로토콜 (데이터 포트)|TCP|
|SSH|22|Secure Shell|TCP|
|SMTP|25|Simple Mail Transfer Protocol - 이메일 전송에 사용|TCP|
|DNS|53|Domain Name System - 주소창에 입력한 도메인을 IP주소로 변경|TCP/UDP|
|HTTP|80|HyperText Transfer Protocol - 웹 페이지 전송, 웹 서비스|TCP/UDP|
|IMAP4|143|우리가 흔히 쓰는 이메일 (저장소 관리가 중요)|TCP|
|HTTPS|443|SSL(Secure Socket Layer) 위의 HTTP(인증서를 사용하여 보안접속, 암호화 전송)|TCP|
- https를 통한 인터넷 접속은, 브라우저를 실행 중인 우리 컴퓨터(또는 휴대폰)가 해당 사이트의 서버와 암호화 통신을 하고 있다는 의미이다.

[SSL 참고 링크 1](https://blog.naver.com/skinfosec2000/222135874222)

[SSL 참고 링크 2](https://jins-dev.tistory.com/entry/SSL-%EC%9D%B4%EB%9E%80-SSL-%EC%97%90-%EB%8C%80%ED%95%9C-%EC%A0%95%EB%A6%AC)



<br>
<br>
<br>

## AWS(Amazon Web Services) : DevOps
<br>

> Infra 공부하기.

<br>

|주요 단어|Description|
|--|--|
|프리티어|처음 1년간은 월별 750시간까지의 사용량은 무료이고 그 이상은 추가 과금이 되는 요금제|
|EC2(Elastic Compute Cloud/유연한 컴퓨팅 클라우드)|이 서비스는 CPU사용량(연산횟수)으로 결제하는 것이 아닌 인스턴스를 켜놓은 시간을 기준으로 결제하는 구조이다.|
|CentOS7|-|
|Java11|-|
|S3|-|
|MySQL|-|
|RDS|Relational Database Service|
|ALB|서버 부하 분산|
|인스턴스|간단하게 말해서 가상 컴퓨터 1대|
|SSH|Secure Shell Protocol, 즉 네트워크 프로토콜 중 하나로 컴퓨터와 컴퓨터가 인터넷과 같은 Public Network를 통해 서로 통신을 할 때 보안적으로 안전하게 통신을 하기 위해 사용하는 프로토콜입니다. <br>대표적인 사용의 예 : 데이터 전송, 원격 제어|

<br>
<br>

> 인스턴스
- 애플리케이션을 실행할 수 있는 가상 서버
- CPU, Memory, 스토리지 및 네트워킹 용량의 다양한 조합이 있다.
- 애플리케이션에 사용할 적절한 리소스 조합을 유연하게 선택할 수 있다.
- 인스턴스를 생성하는 첫 단계는 AMI(Amazon Machine Image, 아마존 머신 이미지)를 선택하는 것이다.

<br>
<br>

> 포트(port)

![image](https://user-images.githubusercontent.com/63379459/109893400-f296ac00-7cce-11eb-98a8-151146c5bdc2.png)

- SSH 기본적으로 추가된
- 일단 HTTP, HTTPS 추가

<br>
<br>

> Nginx(Web Server) 이해와 설치

- Igor Sysoev라는 러시아 개발자가 ***동시접속*** 처리에 특화된 ***웹 서버*** 프로그램이다. <br>Apache보다 동작이 단순하고, *전달자* 역할만 하기 때문에 동시접속 처리에 특화되어 있다.
- nginx는 기존 웹서버에서 많은 ***트래픽***을 감당하기 위해서 확정성을 가지고 설계된 비동기 이벤트 드라이븐 방식의 웹서버를 칭한다.
- 프록시 서버 
- [트래픽](./plan03.md)
- AWS는 별도로 방화벽 비활성화 해준게 없음..
- 인스턴스의 public ip로 웹 부라우저 접속을 하면 ***Welcome to nginx!*** 문자
- nginx 접속 완료

<br>

[nginx 이해하기 및 기본 환경설정](https://whatisthenext.tistory.com/123)

[AWS EC2에 NGINX 설치 및 사용하기](https://msyu1207.tistory.com/entry/AWS-EC2%EC%97%90-NGINX-%EC%84%A4%EC%B9%98-%EB%B0%8F-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)

[AWS EC2에 웹서버(Nginx)설치하고 구동하기__Good](https://medium.com/@taeyeolkim/aws-ec2%EC%97%90-%EC%9B%B9%EC%84%9C%EB%B2%84-nginx-%EC%84%A4%EC%B9%98%ED%95%98%EA%B3%A0-%EA%B5%AC%EB%8F%99%ED%95%98%EA%B8%B0-a46a6e9484a8)

<br>
<br>

> MySQL 이해와 설치

[AWS 환경에서 MySQL 설치](https://www.zinnunkebi.com/aws-mariadb-uninstall-mysql-install/)

<br>
<br>

[(AWS환경)MySQL 초기설정 및 워드프레스용 DB생성](https://www.zinnunkebi.com/aws-mysql-setup-dbmake/)

<br>
<br>


> Windows에서 Linux 인스턴스 연결을 위한 PuTTY 사용 방법
- Connection -> SSH -> Auth -> Private key file for authentication -> .ppk 확장자 key 불러오기
- 마지막으로 ***save***를 클릭해주어야 key를 저장해놓고 서버를 open 할 수 있다.

[참고 링크 : PuTTY 접속할 때마다 private key 첨부해야하는 함. ](http://devstory.ibksplatform.com/2017/08/aws-windows-linux-putty.html)

<br>
<br>


> **PuTTY**
- 터미널/단말/콘솔

|topic|p/g|description|
|--|--|--|
|기동 <br>스크립트|PuTTY|SSH 파일 전송 불가|
|파일 <br>올릴때|winSCP|Windows 기반의 환경에서 SFTP, FTP, SSH 등의 프로토콜로 파일을 전송하는 클라이언트 프로그램|

<br>
<br>



[AWS 인스턴스 생성 참고 링크1.](https://itadventure.tistory.com/372)

[AWS 인스턴스 생성 참고 링크2.](https://medium.com/pocs/ec2%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%9C-%EA%B0%84%EB%8B%A8%ED%95%9C-%EC%9B%B9-%EC%84%9C%EB%B2%84-%EB%A7%8C%EB%93%A4%EA%B8%B0-5b3c84c6d54)

[아마존 웹 서비스를 다루는 기술:실무에서 필요한 AWS 클라우드의 모든것!__책 무료 공개](http://pyrasis.com/book/TheArtOfAmazonWebServices)

[DB서버 구축 참고 링크](https://victorydntmd.tistory.com/337)

[RDS 설치 참고 링크](https://smujihoon.tistory.com/85)


<br>
<br>
<br>

### Python으로 서버 다루는 법 습득.

<br>

> 서버에 문제가 있을 경우 
- CPU, Memory에 문제가 없는지 살펴보아야 한다.

<br>
<br>

### Linux 명령어 

<br>

- #### root에서 사용자로 변경
> `su - ec2-user(사용자명)`

- #### 사용자에서 root로 변경
> `sudo su`


- #### Amazon Linux에 Java 11 설치
OpenJDK 8은 기본 yum 리포지토리에서 사용할 수 있으며 OpenJDK 11은 Amazon Linux 2 추가 리포지토리에서 사용할 수 있습니다. 다음 명령을 사용하여 Amazon Linux 시스템에 Java 11 또는 Java 8을 간단히 설치할 수 있습니다.
> `sudo amazon-linux-extras install java-openjdk11`

- #### Amazon Linux에 Java 8 설치
> `sudo yum install java-1.8.0-openjdk`

- #### Java version 확인
> `java -version`

<br>
<br>
<br>

### Vi Editor 명령어

> `파일의 끝(맨 밑)으로 이동할 때 : G`

> `한줄 잘라내기 : dd`

> `두줄 잘라내기 : 2dd`

> `세줄 잘라내기 : 3dd`

> `붙여넣기 : p`

> `한글자 삭제 : x`

> `단어 삭제 : dw`

> `실행취소(뒤로가기) : u`

> `문장 맨 앞으로 이동 : ^`

> `문장 맨 뒤로 이동 : $`

> `현재 커서 위치에 삽입 : i`

> `현재 커서 바로 다음위치에 삽입 : a`

> `현재 줄 다음 위치에 삽입 : o`

> `커서의 아랫라인과 현재 라인을 하나의 라인으로 합침 : shift + j`





<br>
<br>

[vi 유용한 명령어 모음집 Top](https://gom34.tistory.com/1730)

[vi 명령어 참고 링크1](https://blockdmask.tistory.com/25)

[vi 명령어 참고 링크2](https://wayhome25.github.io/etc/2017/03/27/vi/)

[vi 명령어 참고 링크3](https://booolean.tistory.com/346)

[vi 명령어 참고 링크4(연습)](https://velog.io/@sooo/TIL-14.-VIM-vim-%EB%8B%A8%EC%B6%95%ED%82%A4-%EC%A0%95%EB%A6%AC-%EC%97%B0%EC%8A%B5%EC%82%AC%EC%9D%B4%ED%8A%B8)

[vi를 효과적으로 공부하는 방법 링크5](https://godsman.tistory.com/entry/%ED%88%AC%EC%97%94%ED%8F%AC%EC%97%94-vi%EB%A5%BC-%ED%9A%A8%EA%B3%BC%EC%A0%81%EC%9C%BC%EB%A1%9C-%EC%97%B0%EC%8A%B5%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95%EC%9D%80)


<br>
<br>
<br>


## 갖고놀기

| topic | description |
|--|--|
| F12 | Chrome |
| Postman | 옵션이 많음 |

<br>
<br>
<br>

## CR.LF
> CR : Carriage Return(\r)
- 캐리지 리턴(carriage return) 또는 간단히 리턴(return)은 문자의 새 줄을 시작하는 데 쓰이는 제어 문자나 그 구조를 가리킨다. 컴퓨터 환경에서는 간단히 CR로 줄여 쓴다. 

> LF : Line Feed(\n)
```
해당 용어(CR, LF)와 이 용어들의 조합(CRLF)은 새로운 줄 (New line) 으로 바꾸는 방식을 의미한다. 

CR 과 LF 는 타자기 시절 부터 줄바꿈을 위해 사용하던 방식인데 각각의 의미는 다음과 같다. 

CR : 현재 커서를 줄 올림 없이 가장 앞으로 옮기는 동작
LF : 커서는 그 자리에 그대로 둔 상황에서 종이만 한 줄 올려 줄을 바꾸는 동작

이 방식(CR + LF)은 타자기 이후 컴퓨터에서도 줄바꿈을 의미할 때도 사용되었으나, 줄바꿈을 할 때 굳이 2 byte 를 사용할 필요가 없기에 메모리/Storage 절약을 위해 CR 혹은 LF 만 사용하기도 하였다.

대표적으로 Microsoft 사의 Windows 는 CRLF (\r\n) 을 기본으로 사용하는 반면 
Unix/Linux 에서는 LF (\n) 만으로 줄바꿈을 하고 있다. 
(Mac 의 초기 버전, 9 버전 이하는 CR (\r) 을 줄바꿈으로 사용)

좀 더 명확히 얘기하자면 해당 시스템에서 사용하는 default (기본) 방식이 그렇다는 것이지 반드시 해당 시스템에서는 해당 방식을 사용해야한다는 것은 아니다. 

```


<br>
<br>
<br>

> 매출 1조 기업 -> 유니콘 기업


<br>
<br>
<br>

# 암호화 기술

| topic | description |
| -- | -- |
| RSA |개인키(비밀키)와 공개키 방식) / 인증서에 사용되며 현존하는 가장 안전한 암호화 기술이지만 최근에는 이것도 뚫리고 있다는 / 고가 |
| 대칭키 |키가 있는 / 키관리 / 키로 원문 그대로 사용 가능|
|해시| 복호화가 어렵다 |

<br>
<br>
<br>

- 대칭키는 한국/미국에 여러가지 알고리즘이 많이 존재.
- 대칭키는 키를 관리 해야하기 때문에 DBA(저장)/DevOps(키관리)/개발자 로 나누어 서로 업무를 분담.
- 서로 업무를 모르기 때문에 DB 접근 권한도 제한되며, 알고리즘의 로직도 알 수 없어서 보안 강화.

<br>
<br>


## HW (hardware)

<br>
<br>

### 보조기억장치(HDD / SSD)

<br>

> HDD ( Hard Disk Drive)
- 자기 디스크. 물리적으로 읽는다(LP판 처럼)

```
HDD에서 정보 입출력이란 정보를 저장해두는 원판을 플래터가 움직여 읽어내는 것인데, 이 플래터가 움직이는 거리가 멀어질수록 자연히 정보를 읽고 쓰는 속도가 느려질 수밖에 없습니다. 실제로 그만큼의 거리를 물리적으로 움직여야 하기 때문인데요. 그래서 아무리 다른 컴퓨터 부품이 비약적으로 발전해도 HDD의 물리적 탐색 시간이 병목현상을 일으켜 급격히 느려지는 문제 때문에 실질적인 정보 처리 속도 상승은 기대하기가 어려웠습니다.
```

<br>
<br>

> SSD ( Solid State Drive ) / 고체(반도체) 상태 저장소
- SSD를 USB의 대용량 버전으로도 볼 수 있다.
- 물리적인 정보 저장(전자적 정보 저장)이 아닌 플래시 메모리이다.
- 보조기억장치

<br>

[HDD / SSD 설명 참고 이동](https://trendtalk.co.kr/%EC%A0%95%EB%B3%B4/hdd-ssd-%EC%B0%A8%EC%9D%B4-%EB%B0%8F-%EC%9E%A5%EB%8B%A8%EC%A0%90-%EB%B9%84%EA%B5%90/)


<br>
<br>

> RAM ( Random Access Memory )
- 컴퓨터 전원을 켤 때 메모리는 코드 한 줄도 없이 텅빈 상태로 시작한다.
- 컴퓨터가 빠른 액세스를 하기 위해 데이터를 단기간 저장하는 구성 요소.
- 컴퓨터의 많은 작업이 메모리에 의존하기 때문에 **RAM 용량**은 시스템의 성능 속도에 매우 중요한 역할을 한다.
- 휘발성 메모리로, 작업 중인 파일을 한시적으로 저장한다.
- RAM에 기계어로 작성된 실행코드가 올라가 있어야 중앙처리장치(CPU)가 무엇인가를 실행할 수 있다.


> ROM ( Read Only Memory )
- 컴퓨터 부팅 후 RAM은 텅텅 비어있다.
- 그런 이유로 CPU에게 전원을 켜자마자 제일 먼저 ROM에 들르라고 일러두어 CPU는 ROM을 제일 먼저 읽기 시작한다.
- 읽기 전용 메모리.
- 롬은 읽기만 가능해서 내용을 바꾸기 위해서는 컴퓨터를 분해해서 칩을 교체해야 한다. 대신 읽기 뿐만 아니라 쓰기도 가능한 *플래시 메모리(Flash Memory)*를 사용한다.
- 컴퓨터에 지시사항을 영구히 저장하는 비휘발성 메모리.


> CPU ( Central Processing Unit )

> 보통 CPU를 Processor라고 부르기도 한다.


- 사람의 두뇌와 같이 컴퓨터 시스템에 부착된 모든 장치의 동작을 제어하고 명령을 실행하는 장치.
- 중앙처리장치에는 제어장치, 연산장치, 레지스터 그리고 이들을 연결하여 데이터를 전달하는 버스로 구성되어 있다.

<br>

[CPU 설명 참고 이동](https://coding-factory.tistory.com/351)

<br>
<br>
<br>

> BIOS ( Basic Input/Output System )
- 기본적인 입출력을 담당하는 소프트웨어.

  ex) 키보드, 하드디스크, 메모리 등 잘 연결되어 있는지를 확인하는 일을 한다.
- *바이오스*는 컴퓨터 전원이 켜지자마자 실행되는 '소프트웨어'이기 때문에 기억력이 좋은 롬(ROM)에 저장되어 있어야 한다.
- 롬은 크기가 작아 UI가 들어가지 않은 검은 바탕에서 실 행된다.
- 하드웨어와 아주 밀접한 관계가 있기 때문에 *펌웨어* 라고 부른다.
- 기본적이지 않은 장치들은 덩치가 큰 *운영체제* 가 맡는다.

<br>
<br>

> 부트로더( bootloader)
- 바이오스(BIOS)가 일을 마치면, 부트로더라는 조그만 소프트웨어가 실행된다.
- 운영체제 부팅을 위해 바이오스가 부트로더로 바통을 넘기는 순간이다.
- 운영체제를 깨우려면 운영체제의 코드들이 메모리에 올려져야 한다.
- 이런 막중한 일을 부트로더가 담당한다.
- BIOS와 bootloader의 협력으로 운영체제가 메모리에 무사히 올라가면 부팅(Booting)미션 완료로 운영체제 바탕화면이 보인다면 운영체제가 실행될 준비가 되었다는 신호이다.

<br>
<br>
<br>

## 컴퓨터 부팅 과정
바이오스 -> 부트로더 -> 운영체제











# 파이썬 기반 웹 프로그래밍

# 목표
    - 단계
        - 기획
        - 스토리보드
        - 디자인 시안, 데이터베이스 모델링, 빠르게 프로토타입 생성(끝까지 가봄)
        - 프론트
            - 디자인 진행(페이지 단위 계산), html 코딩, 스크립트 처리
            - React or Vue or Angular : 전면, 부분 구성
        - 백엔드
            - 기능별 구현
                - 페이지별 진행 -> url을 준비 (ex) 만약, 10개라면)
                - 모델 서빙, 머신러닝(딥러닝 관련) 서비스 삽입
                - 데이터 분석, 시각화 -> 파이썬 기반 웹에서 가지는 장점(파이썬이라는 언어로 구성)
            - 공통 기능 구현
            - 통신 프로토콜 구현
                - 요청 응답 처리
        - 데이터베이스
            - DB 설계
            - 테이블 구성
            - 쿼리 구성

    - 웹 환경 이해 및 웹 프로그램 구성 이해
    - flask 기반 웹기반 백엔드(서버)프로그래밍
    - blueprint를 이용한 기능별 분할 구성
    * 블루프린트(blueprint)는 보통 객체지향 프로그래밍에서 "청사진"을 뜻하는 용어인데 플라스크에서는 URL과 함수의 매핑을 관리하기 위해 사용하는 도구(클래스)이다.
        - 회원관련 업무(가입, 로그인, 로그아웃, 탈퇴, 세션관리, 쿠키, ...) : A개발자 담당
        - 모델 서빙 파트(데이터 전처리, 모델 예측 수행, 응답처리 등등) : B개발자 담당
        - 데이터베이스 관련 업무(sql or ORM 준비, API 준비, 데이터베이스 준비) : C개발자 담당(DBA 업무 포함)
    - 데이터베이스 연동 (sql, ORM)
    - 배포 및 운영
        - 실제 회사, 개발팀 개발 완료 => 전달 => 운영팀이 세팅 운영/유지보수 진행

# 발전적 목표
    - 머신러닝(딥러닝 포함) 모델 서빙및 서비스를 구현
    - 구축된 서비스를 도커 및 쿠버네티스 기반하에서 운영
    - MLOps에 연동사용

# 가상환경 구축
    - 순수 파이썬
        - 가상환경을 모아두는 폴더 생성
            - mkdir venvs
        - 해당폴더 이동
            - cd venvs
        - 가상환경 생성
            - python -m venv 가상환경이름
    - 아나콘다(미니콘다, ..)

# 필요한 패키지 설치
    - requirements.txt 생성
    - 작성
        - 수동
            - 직접 기입
            - 패키지==버전
            - 패키지
        - 자동 : 
            - 개발이 다 종료된 후, 개발중에 생성한다면
                - 패키지가 이미 일부 설치가, 혹은 전부 설치가 되어 있다
                - 내가 설치하지 않은 패키지도 추가된다
            - pip freeze > requirements.txt
    - 설치
        - pip install -r requirements.txt
        - 번외
        - pip를 수행하면 command와 option 안내가 나와 다양한 기능 소개
        - ex)
            - pip show pandas
                - WARNING: Package(s) not found: pandas
                - 해당 패키지가 설치되어 있다면 노출, 없으면 경고, ..

# 데이터베이스 연동
    - 1단계 코드 : 요청시 디비 접속, 쿼리 수행, 접속 해제 => 접속/해제 반복으로 인한 속도 저하문제 존재, 접속이 몰리면 서비스 지연 문제 발생, 다만 쉽게 구현 가능
    - 2단계 코드 : 서버 가동시 sqlalchemy Pool을 이용하여 동접수를 계산하여 커넥션을 생성, 
               요청시 -> 풀에서 커넥션 획득 -> 쿼리 수행 -> 커넥션 반납
               서버 종료시 Pool에 있는 모든 커넥션 해제(반납)
    - 3단계 코드 : flask-migrate -> sqlalchemy -> ORM을 이용하여 객체지향적으로 쿼리 수행
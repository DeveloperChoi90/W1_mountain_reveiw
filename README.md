# W1_mountain_review

## 항해99 첫 미니프로젝트 (참가자 : 김하연, 문성준, 유승연, 최병민)


## 프로젝트 정보

 - 혼자 등산을 하면서 나를 기분좋게 해주었던 산의 사진과 좋았던 코스를 소개하며 혼산러들의 정보를 공유하는 웹페이지입니다.

 - 개발기간 : 22.5.9-5.12
---
## Stack

 - frontend : HTML, CSS,

 - backend : python ,Flask

 - db : mongoDb

 - jQuery, jinja2, javascript
---
## 상세기능
### 메인페이지
1. 메인
 - 사진 및 리뷰등록
 - modal 기능 
 - 사진 클릭 시 상세페이지
 - 검색기능 가능
 - [전체목록 보기] button click 시 이벤트 발생 
2. modal 
 - 등록하기 button click시 이벤트 발생
 - 사진 클릭 시 상세페이지에 작성했던 정보 모달로 call

### 로그인,회원가입

 - 메인 페이지에서 로그인 페이지로 rendering 
 - JWT Token 이용 
 - 회원가입 button 클릭 시 회원가입 button으로 toggle 
 - Bulma 사용

### 상세페이지

1. 등록 종류
 - 사진등록, 산이름, 등산한 코스 이름, 지역명, 편의시설, 소감 및 기타정보 
2. 이벤트
 - num으로 등록 시 경고 이벤트 발생
 ---
 
## API 구성

### 웹페이지의 메인페이지

*> - 메인페이지인 idex.html 파일과 등록된 게시글의 정보를 mongoDB에서 가저와 rendering 해준다.*

```python

@app.route('/')

def home():

```

### 로그인 페이지

*> 로그인페이지 rendering*

```python

@app.route('/login')

def home_login():

```

*>*

# W1_mountain_review

## 항해99 첫 미니프로젝트 (참가자 : 김하연, 문성준, 유승연, 최병민)

## 프로젝트 정보

*> - 혼자 등산을 하면서 나를 기분좋게 해주었던 산의 사진과 좋았던 코스를 소개하며 혼산러들의 정보를 공유하는 웹페이지입니다.*

*> - 개발기간 : 22.5.9-5.12*

## Stack

*> - frontend : HTML, CSS,*

*> - backend : python ,Flask*

*> - db : mongoDb*

*> - jQuery, jinja2, javascript*

## 상세기능

*> - 로그인 / 회원가입*

*> - 로그아웃*

*> - 사진 및 리뷰등록*

*> - modal 기능 - 사진 클릭 시 상세페이지*

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
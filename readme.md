# 파이썬 가상 환경 이용하기

## 가상 환경 디렉토리 생성하기
```commandline
D:\kims> mkdir flaskProject
D:\kims> cd flaskProject
D:\kims\flaskProject>
```

## 가상 환경 만들기
```commandline
D:\kims\flaskProject> python -m venv myProject1
```

## 가상 환경 접근하기
```commandline
D:\kims\flaskProject> cd myProject1
D:\kims\flaskProject\myProject1> cd Scripts
D:\kims\flaskProject\myProject1\Scripts> activate
(myProject1) D:\kims\flaskProject\myProject1\Scripts>
```

## 가상 환경에서 빠져나오기
```commandline
(myProject1) D:\kims\flaskProject\myProject1\Scripts> deactivate
D:\kims\flaskProject\myProject1\Scripts>
```

# 플라스크 시작하기

## 플라스크 설치하기
```commandline
D:\kims\flaskProject\myProject1\Scripts> activate
(myProject1) D:\kims\flaskProject\myProject1\Scripts> python -m pip install --upgrade pip
Collecting pip
  Downloading pip-22.3-py3-none-any.whl (2.1 MB)
.... 생략 ....
Successfully uninstalled pip-21.2.4
Successfully installed pip-22.3
(myProject1) D:\kims\flaskProject\myProject1\Scripts> pip install flask 
```

## 플라스크 프로젝트 배치파일 생성하기
```commandline
D:\kims\flaskProject\myProject1> copy con > myProject.cmd 
@echo off
cd D:/kims/flaskProject/myProject1
D:D:/kims/flaskProject/myProject1/Scripts/activate
```
위와 같이 입력하고, Ctrl-Z 눌러 저장

## 배치파일 실행을 위한 환경 변수 설정하기
```commandline
D:\kims\flaskProject\myProject1> sysdm.cpl
```
```text
[시스템 속성] 창 -> [고급] 탭 -> [환경 변수] 버튼 -> [시스템 변수] 항목
 -> [Path] 변수 항목 -> [환경 변수 편집] 창에서 [새로 만들기] 버튼 ->  
 -> D:\kims\flaskProject\myProject1 값 입력 -> [환경 변수 편집] 창에서 [확인] 버튼
 -> [환경 변수] 창에서 [확인] 버튼 
```

## 플라스크 애플리케이션 파일 생성하기
D:\kims\flaskProject\myProject1에 pybo.py 새로 만들기
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_pybo():
    return 'Hello~! Pybo~!'
```

## 플라스크 애플리케이션 파일 실행하기
```commandline
D:\kim6\flaskProject\myproject1> activate
(venv) D:\kim6\flaskProject\myproject1> set FLASK_APP=pybo
(venv) D:\kim6\flaskProject\myproject1> set FLASK_DEBUG=true
(venv) D:\kim6\flaskProject\myproject1> flask run
```

## 플라스크의 디렉토리 구조
```text
├── pybo/
│      ├─ __init__.py
│      ├─ models.py
│      ├─ forms.py
│      ├─ views/
│      │   └─ main_views.py
│      ├─ static/
│      │   └─ style.css
│      └─ templates/
│            └─ index.html
└── config.py
```

## 플라스크의 주요 파일 설명
| 디렉토리 및 파일명 | 설명                                              |
|------------|-------------------------------------------------|
| config.py | pybo 프로젝트의 환경 변수, 데이터베이스를 설정 |
| models.py  | pybo 프로젝트는 ORM을 지원하는 SQLAIchemy를 사용하여 데이터베이스 처리 |
| forms.py   | WTFomrs 라이브러리를 활용하여 서버로 전송된 폼의 데이터를 처리 |
| views | 파이썬에서 Controller 역할을 하는 view 파일을 저장 |
| static | css(스타일시트), js(자바스크립트), image(이미지) 등을 저장 |
| templates | 파이썬에서 view page 역할을 하는 html 문서 등을 저장 |

## 플라스크의 처리 패턴
```text
자바와 같은 언어는 MVC(Model View Controller)로 구성되지만, 
파이썬은 MCT(Model Controller Templates)로 구성되는데,
```
| JAVA | Python   | 설명 |
|------------|----------|-----------------------------------|
| Model      | Model    | 데이터베이스 처리 |
| View | Template | 클라이언트 브라우저에 표시 |
| Controller | View     | 모델로 부터 처리된 데이터를 받아 템플릿에 표시 | 

```text
클라이언트가 웹 브라우저를 통하여 서버에 특정 데이터 처리를 요청하면, 그 데이터를 컨트롤러인 view에서 받아
모델(models.py)에서 받아 데이터베이스에 저장 및 처리하고, 그 결과를 정해진
스타일과 스크립트에 의해 클라이언트에게 템플릿(view)을 보여주는 형태
Web Browser → forms.py → view(Controller) → models.py(Model) 
 → 데이터베이스 →  static → templates(View) 
```

## pybo.py의 이동 및 변경
```commandline
(venv) D:\kim6\flaskProject\myproject1> mkdir pybo
(venv) D:\kim6\flaskProject\myproject1> move pybo.py pybo/__init__.py
(venv) D:\kim6\flaskProject\myproject1> cd pybo
(venv) D:\kim6\flaskProject\myproject1> flask run
```

## __init__.py 파일 편집
D:\kim6\flaskProject\myproject1\pybo>__init__.py 파일 내용 수정
```python
from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_pybo():
        return 'Hello~! Pybo~!'

    return app
```

# 블루프린트를 활용한 프로젝트 다루기

## 블루프린트 생성하기
```commandline
(venv) D:\kim6\flaskProject\myproject1>cd pybo
(venv) D:\kim6\flaskProject\myproject1\pybo>mkdir views
```

D:\kim6\flaskProject\myproject1\pybo\views\main_view.py 파일 작성
```python
from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def hello_pybo():
    return 'Hello~! Pybo~!'
```

## 블루프린트 등록하기
D:\kim6\flaskProject\myproject1\pybo>__init__.py 파일 내용 수정
```python
from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app
```

## 블루프린트에 라우팅 함수 추가
D:\kim6\flaskProject\myproject1\pybo\views\main_view.py 파일 내용 수정
```python
from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello~! Pybo~!'


@bp.route('/')
def index():
    return 'Pybo index'
```

## 블루프린트 동작 확인
```commandline
(venv) D:\kim6\flaskProject\myproject1\pybo> cd ..
(venv) D:\kim6\flaskProject\myproject1> flask run 
```

# 모델 생성하기

## ORM 라이브러리 설치하기
```commandline
(venv) D:\kim6\flaskProject\myproject1> pip install flask-migrate
```

## ORM 설정 파일 추가하기
D:\kim6\flaskProject\myproject1\config.py 파일 생성
```python
import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

## ORM 적용하기
D:\kim6\flaskProject\myproject1\pybo\__init__.py 파일 수정
```python
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    # 블루프린트
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app
```

## 데이터베이스 초기화
```commandline
(venv) D:\kim6\flaskProject\myproject1> set FLASK_APP=pybo
(venv) D:\kim6\flaskProject\myproject1> set FLASK_DEBUG=true
(venv) D:\kim6\flaskProject\myproject1> flask db init
```
위 명령으로 데이터베이스를 관리하는 초기 파일들을 migrations 디렉터리에 자동으로 생성
파이참의 Project 패널을 확인해보면 myProject1 디렉토리에 migrarions 디렉토리가 생성됨을 알 수 있음

## 데이터베이스 관리 명령어
| 명령 | 설명 |
|----------------------|--------------------------------------------------|
| flask db migrate | 모델을 새로 생성하거나 변경 |
| flask db upgrade | 모델의 변경 내용을 실제 데이터베이스에 적용 |

# 모델 만들기

## 모델 컬럼(속성) 규정하기
D:\kim6\flaskProject\myproject1\pybo\models.py 파일 생성
```python
from pybo import db

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
```

D:\kim6\flaskProject\myproject1\pybo\__init__.py 파일 수정
```python
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # 블루프린트
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app
```

## 변경된 데이터베이스 적용하기
```commandline
(venv) D:\kim6\flaskProject\myproject1> flask db migrate
(venv) D:\kim6\flaskProject\myproject1> flask db upgrade
```

## 데이터베이스 확인하기

### DB Browser for SQLite 설치하기
https://sqlitebrowser.org/dl 에 접속하여 해당 운영체제에 맞는 버전을 설치하도록 한다.

### DB Browser for SQLite 에서 pybo.db 열기
    실행된 DB Browser에서 [파일] > [데이터베이스 열기] > 저장된 D:\kim6\flaskProject\myproject1\pybo.db 를 연다.

## 데이터베이스 모델 활용하기
```commandline
-- 데이터 추가하기 --
(venv) D:\kim6\flaskProject\myproject1> flask shell
>>> from pybo.models import Board
>>> from datetime import datetime
>>> b = Board(subject='테스트글1 입니다.', content='테스트1에 대한 내용입니다.', create_date=datetime.now())
>>> from pybo import db
>>> db.session.add(b)
>>> db.session.commit()
>>> b.id
>>> b = Board(subject='테스트글2 입니다.', content='테스트2에 대한 내용입니다.', create_date=datetime.now())
>>> from pybo import db
>>> db.session.add(b)
>>> db.session.commit()
>>> b.id
-- 데이터 조회하기 --
>>> Board.query.all()
>>> Board.query.filter(Board.id==2).all()
>>> Board.query.filter(Board.subject.like('%테스트%')).all()
-- 데이터 수정하기 --
>>> b = Board.query.get(2)
>>> b
>>> b.subject = '더미 데이터2 입니다.'
>>> db.session.commit()
-- 데이터 삭제하기 --
>>> b = Board.query.get(1)
>>> db.session.delete(b)
>>> db.session.commit()
```

# 게시판 목록 기능 구현하기

## 게시판 뷰 수정하기
D:\kim6\flaskProject\myproject1\pybo\views\main_views.py 파일 수정
```python
from flask import Blueprint, render_template
from pybo.models import Board

bp = Blueprint('main', __name__, url_prefix='/')

# 웹 브라우저에서 localhost:5000/hello 요청시
@bp.route('/hello')
def hello_pybo():
    return 'Hello~! Pybo~!'

# 웹 브라우저에서 localhost:5000 요청시
@bp.route('/')
def index():
    board_list = Board.query.order_by(Board.create_date.desc())
    return render_template('board/board_list.html', board_list=board_list)

@bp.route('/detail/<int:board_id>/')
def detail(board_id):
    board = Board.query.get(board_id)
    return render_template('board/board_detail.html', board=board)
```

## 게시판 템플릿 작성하기
```commandline
(venv) D:\kim6\flaskProject\myproject1> cd pybo
(venv) D:\kim6\flaskProject\myproject1\pybo> mkdir templates
(venv) D:\kim6\flaskProject\myproject1\pybo> cd templates
(venv) D:\kim6\flaskProject\myproject1\pybo\templates> mkdir templates
```

D:\kim6\flaskProject\myproject1\pybo\templates\board\board_list.html 파일 작성
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>게시글 목록</title>
</head>
<body>
<!-- 게시글 목록 -->
{% if board_list %}
    <ul>
    {% for board in board_list %}
        <li><a href="/detail/{{ board.id }}/">{{ board.subject }}</a></li>
        <li>{{ board.create_date }}</li>
    {% endfor %}
    </ul>
{% else %}
    <p>게시글이 없습니다.</p>
{% endif %}
</body>
</html>
```

D:\kim6\flaskProject\myproject1\pybo\templates\board\board_detail.html 파일 작성
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>게시글 상세보기</title>
</head>
<body>
<h1>{{ board.subject }}</h1>
<div>
    {{ board.content }}
</div>
<div>
    <a href="../../">목록으로 이동</a>
</div>
</body>
</html>
```

```commandline
(venv) D:\kim6\flaskProject\myproject1> flask run
```

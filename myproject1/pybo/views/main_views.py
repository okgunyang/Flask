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
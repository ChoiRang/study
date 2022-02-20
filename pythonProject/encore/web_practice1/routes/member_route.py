from flask import Blueprint, request, render_template, session
from encore.web_practice1.member.member_service import MemberService
from encore.web_practice1.member.member_vo import MemberVo

bp = Blueprint('member', __name__, url_prefix='/member')
service = MemberService()


@bp.get('/join')		# /member/join: get
def join_form():		#회원가입 양식을 줌
	return render_template('member/join.html')


@bp.post('/join')
def join():				# 회원가입 양식에 작성하고 가입버튼 누름요청, 가입완료
	id = request.form['id']
	pwd = request.form['pwd']
	name = request.form['name']
	email = request.form['email']
	service.insert_user(MemberVo(id, pwd, name, email))
	return render_template('index.html')


@bp.get('/login')
def login_form():
	return render_template('member/login.html')


@bp.post('/login')
def login():
	id = request.form['id']
	pwd = request.form['pwd']
	login_check = service.login(id, pwd)
	if login_check is None:
		msg = '없는 아이디'
	else:
		session['flag'] = True
		session['login_id'] = id
		msg = '로그인 정상 처리'
	return render_template('member/result.html', msg=msg)


@bp.get('/logout')
def logout():
	session.clear()
	session['flag'] = False
	return render_template('index.html')


@bp.get('/my_info/<string:user_id>')
def my_info(user_id):
	user_vo = service.get_my_info(user_id)
	return render_template('member/info.html', user_vo=user_vo)


@bp.get('/modify/<string:user_id>')
def modify_user_form(user_id):
	user_vo = service.get_my_info(user_id)
	return render_template('member/modify_user.html', user_vo=user_vo)


@bp.post('/modify_user/<string:user_id>')
def modify_user(user_id):
	pwd = request.form['pwd']
	name = request.form['name']
	email = request.form['email']
	service.modify_user(MemberVo(user_id, pwd, name, email), user_id)
	user_vo = service.get_my_info(user_id)
	return render_template('member/info.html', user_vo=user_vo)


@bp.get('/resign/<string:user_id>')
def resign_user(user_id):
	service.resign_user(user_id)
	session.clear()
	session['flag'] = False
	return render_template('index.html')

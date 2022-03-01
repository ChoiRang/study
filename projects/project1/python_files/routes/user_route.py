from flask import render_template, Blueprint, request, session
from python_files.user.user_service import UserService
from python_files.user.user_vo import UserVo

bp = Blueprint('user', __name__, url_prefix='/user')
service = UserService()


@bp.get('/sign_page')
def sign_user():
	return render_template('user/user_sign_form.html')


@bp.post('/id_check')
def id_check():
	user_id = request.form['user_id']
	check = service.id_check(user_id)
	return render_template('user/user_sign_form.html', check=check, user_id=user_id)


@bp.post('/password_check')
def password_check():
	user_id = request.form['user_id']
	password_1 = request.form['user_password']
	password_2 = request.form['user_password_check']
	if user_id is None:
		if password_1 == password_2:
			return render_template('user/user_sign_form.html', password_1=password_1, password_2=password_2, pw_check=1)
		else:
			return render_template('user/user_sign_form.html', pw_check=0)
	else:
		if password_1 == password_2:
			return render_template('user/user_sign_form.html', user_id=user_id, password_1=password_1, password_2=password_2, pw_check=1)
		else:
			return render_template('user/user_sign_form.html', user_id=user_id, pw_check=0)


@bp.post('/sign_action')
def sign_action():
	user_id = request.form['user_id']
	user_password = request.form['user_password']
	nick_name = request.form['nick_name']
	print(user_id, user_password, nick_name)
	service.sign_user(UserVo(user_id=user_id, user_password=user_password, nick_name=nick_name))
	return render_template('welcome.html')


@bp.get('/login')
def login_form():
	return render_template('user/user_login_form.html')


@bp.post('/login_action')
def login_action():
	user_id = request.form['user_id']
	user_password = request.form['user_password']
	login_check = service.login_user(user_id, user_password)
	if login_check is None:
		msg = '아이디와 비밀번호가 다릅니다'
		return render_template('user/user_login_form.html', msg=msg)
	else:
		if login_check.user_password == user_password:
			session.login_id = login_check.user_id
			session.login_status = True
			return render_template('welcome.html')
		else:
			msg = '아이디와 비밀번호가 다릅니다'
			return render_template('user/user_login_form.html', msg=msg)


@bp.get('/logout_action')
def logout_action():
	session.clear()
	return render_template('welcome.html')


@bp.get('/myinfo')
def user_info_form():
	return render_template('user/user_info_form.html')

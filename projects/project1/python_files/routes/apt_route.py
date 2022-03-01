import pandas as pd
from flask import render_template, Blueprint, request, session
from python_files.extract_legal_code import ExtractLegalCode
from python_files.apart.apart_service import ApartService
import json


bp = Blueprint('apt', __name__, url_prefix='/apt')
extract = ExtractLegalCode()
apart_service = ApartService()

@bp.get('/main')
def apt_main_form():
	local1 = extract.extract_local()
	return render_template('apt/apt_form.html', local=local1)


@bp.post('/getLocal/<string:local>')
def get_info(local):
	local_first = json.loads(local)
	return render_template('apt/apt_main_form', local_first=local_first)


@bp.post('/generate')
def get_api():
	local_first = request.form['local_first']
	local_second = request.form['local_second']
	date = request.form['date']
	date = str(date)
	legal_code = extract.extract_local_code(local_first, local_second)
	res = apart_service.get_apt(legal_code, date)
	apart_df = pd.DataFrame(res)			# dict -> dataframe
	length = len(apart_df)
	if res is None:
		msg = '정보를 다시 입력해 주세요'
		print(msg)
		return render_template('welcome.html', msg=msg)
	else:
		print('success')
		return render_template('welcome.html', apt_info=apart_df, search=True, length=length)

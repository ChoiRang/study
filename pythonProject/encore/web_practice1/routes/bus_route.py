from flask import Blueprint, request, render_template
from encore.web_practice1.bus_info.bus_service import BusService

# 블루프린트 객체 생성: 라우트 등록
bp = Blueprint('bus', __name__, url_prefix='/bus')
# 버스와 관련된 기능 제공 클래스
bus_service = BusService()


@bp.route('/bus_info', methods=['POST'])
def bus_info():
	busnm = request.form['busnm']						# 폼 양식의 이름이 'busnm' 인 요소의 값을 읽는다
	res = bus_service.get_bus_info_by_name(busnm)
	return render_template('bus/bus_list.html', res=res, flag=True)


@bp.route('/station_info/<string:bus_id>')
def station_info(bus_id):
	res = bus_service.get_station_info_by_id(bus_id)
	return render_template('bus/station_list.html', res=res)

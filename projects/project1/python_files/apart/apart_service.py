from python_files.keys import keys
from bs4 import BeautifulSoup
import requests


class ApartService:
	def __init__(self):
		self.key = keys.APT_TRADE_ENCODING_KEY

	def get_apt(self, local_code, date):
		url = f"http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?LAWD_CD={local_code}&DEAL_YMD={date}&serviceKey={self.key}"
		html = requests.get(url).text
		bs = BeautifulSoup(html, 'lxml-xml')
		header_code = bs.find('totalCount').text

		if header_code == '0':
			msg = bs.find('resultMsg').text
			print(msg)
			return
		route_list = bs.find_all('item')
		apt_list = []
		for apt_info in route_list:
			dong = apt_info.find('법정동').text
			apart_name = apt_info.find('아파트').text
			build_year = apt_info.find('건축년도').text
			trade_value = apt_info.find('거래금액').text
			apart_area = apt_info.find('전용면적').text
			year = apt_info.find('년').text
			month = apt_info.find('월').text
			day = apt_info.find('일').text
			apt_list.append([dong, apart_name, build_year, trade_value, apart_area, year, month, day])

		return apt_list


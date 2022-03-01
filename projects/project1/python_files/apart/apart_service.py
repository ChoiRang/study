from python_files.keys import keys
from bs4 import BeautifulSoup
from python_files.apart.apart_vo import ApartVo
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
		res = {}
		list1 = []
		list2 = []
		list3 = []
		list4 = []
		list5 = []
		list6 = []
		list7 = []
		list8 = []
		for apt_info in route_list:
			dong = apt_info.find('법정동').text
			apart_name = apt_info.find('아파트').text
			build_year = apt_info.find('건축년도').text
			trade_value = apt_info.find('거래금액').text
			apart_area = apt_info.find('전용면적').text
			year = apt_info.find('년').text
			month = apt_info.find('월').text
			day = apt_info.find('일').text
			list1.append(dong)
			list2.append(apart_name)
			list3.append(build_year)
			list4.append(trade_value)
			list5.append(apart_area)
			list6.append(year)
			list7.append(month)
			list8.append(day)
		res['dong'] = list1
		res['apart_name'] = list2
		res['build_year'] = list3
		res['trade_value'] = list4
		res['apart_area'] = list5
		res['year'] = list6
		res['month'] = list7
		res['day'] = list8

		return res


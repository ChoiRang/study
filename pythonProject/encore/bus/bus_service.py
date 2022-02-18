import pandas as pd
import requests
from bs4 import BeautifulSoup

from encore.bus.bus_vo import BusVo


class Bus:

	def __init__(self):
		self.key = '0o1h3rwXg2ba8nhNfKw6gI%2Bnuoln2ZsGWGvk3AoS4KLLQwgfu4xkKYi9Q2z9jpE%2BuJA%2FMMUAUEBBTCxhMpfEJQ%3D%3D'

	def bus_info(self):
		try:
			bus_info = pd.read_excel('서울시 버스노선ID 정보(20210520).xlsx')
			bus = input('버스 노선 입력: ')
			bus_code = bus_info[bus_info['노선명'] == bus]['ROUTE_ID'].values[0]
			return bus_code
		except Exception as e:
			return None

	def get_bus_route(self, bus_code):
		res = []
		bus_type = ['공용', '공항', '마을', '간선', '지선', '순환', '광역', '인천', '경기', '폐지']
		if bus_code is None:
			res.append('없는 번호입니다')
			return res
		url = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getRouteInfo?'
		url += 'ServiceKey=' + self.key
		url += '&busRouteId=' + str(bus_code)
		result = requests.get(url).text
		soup = BeautifulSoup(result, 'lxml-xml')

		route_type = soup.find('routeType').get_text()
		start_station = soup.find('stStationNm').get_text()
		end_station = soup.find('edStationNm').get_text()
		term = soup.find('term').get_text()
		route_type = int(route_type)

		for i, b_type in enumerate(bus_type):
			if i == route_type:
				route_type = b_type
		res.append(
			BusVo(
				bus_code=bus_code,
				bus_route_type=route_type,
				start_station=start_station,
				end_station=end_station,
				term=term
			)
		)

		return res

	def get_station(self, bus_code):
		try:
			res = []

			url = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?'
			url += 'ServiceKey=' + self.key
			url += '&busRouteId=' + str(bus_code)
			result = requests.get(url).text
			soup = BeautifulSoup(result, 'lxml-xml')

			station = soup.find_all('stationNm')
			for std in station:
				res.append(std.get_text())
			# 중복검사
			res = list(set(res))

			return res
		except Exception as e:
			print(e)

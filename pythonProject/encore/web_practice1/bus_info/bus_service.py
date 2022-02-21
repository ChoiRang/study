import requests
from bs4 import BeautifulSoup
from encore.web_practice1.bus_info.bus_vo import BusVo, Station
from encore.web_practice1.bus_info.bus_dao import BusDao


class BusService:
	def __init__(self):
		self.key = '0o1h3rwXg2ba8nhNfKw6gI%2Bnuoln2ZsGWGvk3AoS4KLLQwgfu4xkKYi9Q2z9jpE%2BuJA%2FMMUAUEBBTCxhMpfEJQ%3D%3D'
		self.dao = BusDao()

	def get_bus_info_by_name(self, bus_code):
		url = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?'
		url += 'ServiceKey=' + self.key
		url += '&strSrch=' + bus_code
		result = requests.get(url).text
		soup = BeautifulSoup(result, 'lxml-xml')

		header_code = soup.find('headerCd').text
		if header_code != '0':
			msg = soup.find('headerMsg').text
			print(msg)
			return

		route_list = soup.find_all('itemList')
		res = []
		for route in route_list:
			bus_route_id = route.find('busRouteId').text
			bus_route_name = route.find('busRouteNm').text
			start_station_name = route.find('stStationNm').text
			end_station_name = route.find('edStationNm').text
			bus_first_time = route.find('firstBusTm').text
			bus_last_time = route.find('lastBusTm').text
			term = route.find('term').text
			res.append(
				BusVo(
					bus_code=bus_route_id,
					bus_route_name=bus_route_name,
					start_station=start_station_name,
					end_station=end_station_name,
					start_time=bus_first_time,
					end_time=bus_last_time,
					term=term
				)
			)
		return res

	def get_station_info_by_id(self, bus_id):
		url = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?'
		url += 'ServiceKey=' + self.key
		url += '&busRouteId=' + bus_id
		result = requests.get(url).text
		soup = BeautifulSoup(result, 'lxml-xml')
		header_code = soup.find('headerCd').text

		if header_code != '0':
			msg = soup.find('headerMsg').text
			print(msg)
			return
		station_list = soup.find_all('itemList')
		res = []

		for station in station_list:
			seq = station.find('seq').text
			station_name = station.find('stationNm').text
			bus_direction = station.find('direction').text
			gps_x = station.find('gpsX').text
			gps_y = station.find('gpsY').text
			res.append(
				Station(
					seq=seq,
					station_name=station_name,
					direction=bus_direction,
					gps_x=gps_x,
					gps_y=gps_y
				)
			)

		return res

	def generate_bus_member(self, bus_id, bus_name, user_id):
		check = self.dao.insert_info(bus_id, bus_name, user_id)
		return check

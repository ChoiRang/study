
from encore.web_practice1.bus_info.bus_service import Bus

if __name__ == '__main__':
	bus = Bus()
	bus_name = input('버스 노선 입력: ')
	res = bus.bus_info(bus_name)
	if res is None:
		print('없는 번호입니다.')
	else:
		res1 = bus.get_bus_route(res)
		for i in res1:
			print(i)
		res2 = bus.get_station(res)
		print('=====정류장=====')
		for idx, i in enumerate(res2):
			if idx % 5 == 0:
				print(i)
			else:
				print(i, end=', ')

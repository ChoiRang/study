def solution(bridge_length, max_weight, truck_weight):
	time = 0  # 1. 마지막 트럭를 제외한 모든 트럭이 다리를 통과하는데 걸리는 시간
	total_weight = 0  # 2. 현재 다리위에 있는 트럭 무게의 총합
	bridge = [0] * bridge_length  # 3. 다리->큐로 구현

	# 트럭 다리 위에 올리기
	while len(truck_weight) > 0:
		tmp = bridge.pop(0)  # 그냥 pop 할 경우 맨 뒤에값을 빼기때문에 pop(0), 시간복잡도 : O(N)
		total_weight -= tmp  # 총 무게에서 빠져나간 트럭의 무게가 제거됨
		# case2 개 , 현재 트럭무게의 총합 + 대기1번의 무게 > 최대하중
		if total_weight + truck_weight[0] > max_weight:
			bridge.append(0)  # 무게가 0인 트럭(계산용)
		else:
			truck = truck_weight.pop(0)
			total_weight += truck
			bridge.append(truck)
		time += 1
	# truck_weight =[] 되는 순간 끝나므로 지나가는 시간 +
	return time + bridge_length


from collections import deque


def solution2(bridge_length, weight, truck_weight):
	time = 0
	total_weight = 0
	bridge = deque(0 for _ in bridge_length)
	truck_weight.reverse()

	while truck_weight:  # 다 배면 null 이 되서 종료됨
		tmp = bridge.popleft()
		total_weight -= tmp
		if total_weight + truck_weight[-1] > weight:
			bridge.append(0)
		else:
			truck = truck_weight.pop()
			bridge.append(truck)
			total_weight += truck
		time += 1
	return time + bridge_length

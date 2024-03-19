import collections
import heapq
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for start, end, price in flights:
            graph[start].append([end, price])

        # 무한 사이클 방지용
        visit = {}
        # (가격, 출발지, 종착지 카운트), heapq(우선순위 정렬)로 최솟값을 항상 앞으로 정렬
        heap = []
        heapq.heappush(heap, (0, src, 0))

        while heap:
            total_price, node, count = heapq.heappop(heap)

            if node == dst:
                return total_price
            if node not in visit or visit[node] > count:
                visit[node] = count
                for end, price in graph[node]:
                    if count <= k:
                        heapq.heappush(heap, (total_price + price, end, count + 1))

        return -1

# testcase 중 무한 루프를 도는 3 -> 12 -> 6 -> 3 의 무한루프가 있음

from typing import *
import heapq


# ref
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        MAX = 10**20
        end_x, end_y = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        times = [[MAX]*end_y for _ in range(end_x)]
        heap = []
        heapq.heappush(heap, (0, 0, 0))
        # 기본 종료 조건
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        while len(heap) > 0:
            time, x, y = heapq.heappop(heap)
            if x == end_x-1 and y == end_y-1:
                return time
            # 해당 좌표의 시간이 총 시간 보다 낮을 경우 패스
            if times[x][y] < time:
                continue
            # 상하좌우 값 계산
            for dir_x, dir_y in directions:
                new_x, new_y = x+dir_x, y+dir_y
                # x, y의 범위 초과 조절
                if 0 <= new_x < end_x and 0 <= new_y < end_y:
                    next_time = grid[new_x][new_y]
                    # 다음 셀의 시간이 현재 시간+1 초 이하일때
                    if next_time <= time+1:
                        # times 해당 셀의 시간 확인
                        if times[new_x][new_y] > time+1:
                            heapq.heappush(heap, (time+1, new_x, new_y))
                            times[new_x][new_y] = time+1
                    else:
                        # 다음 지점으로 갈 수 없을때 왕복하기 (time 늘리기용)
                        # 다음 셀과 현재 셀의 시간 차이 계산)2배수인지 -> 짝수일 경우 이전 셀과 현재 샐을 왕복하여 최단시간으로 시간을 맞출수 있다.
                        if time % 2 == next_time % 2:
                            next_time += 1  # new_x & new_y 는 바로 옆칸이므로, +1
                        if times[new_x][new_y] > time:
                            heapq.heappush(heap, (next_time, new_x, new_y))     # time 갱신
                            times[new_x][new_y] = next_time

        return -1


# timeout?
class Solution1:
    def minimumTime(self, grid: List[List[int]]) -> int:
        end_x, end_y = len(grid)-1, len(grid[0])-1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        heap = []
        heapq.heappush(heap, (0, 0, 0))

        while len(heap) > 0:
            time, x, y = heapq.heappop(heap)
            if x == end_x and y == end_y:
                return time

            for dir_x, dir_y in directions:
                new_x, new_y = x+dir_x, y+dir_y

                if 0 <= new_x <= end_x and 0 <= new_y <= end_y:
                    if grid[new_x][new_y] <= time+1:
                        heapq.heappush(heap, (time+1, new_x, new_y))

        return -1

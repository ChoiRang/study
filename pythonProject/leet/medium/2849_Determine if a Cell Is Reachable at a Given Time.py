class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy:
            return t != 1
        x, y = abs(fx-sx), abs(fy-sy)

        if max(x, y) <= t:
            return True

        return False

"""
시간이 2초 이상일 경우 원하는 시간대에 원하는 지점 도착이 가능하다. (L3: 예외사항) 
대각선 이동이 가능하기에 목적지 까지의 최소 시간 ( max(x, y) )을 만족하면 도착 시간 조정이 가능하다.
"""
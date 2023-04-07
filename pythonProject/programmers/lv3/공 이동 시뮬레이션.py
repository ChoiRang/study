import collections


def solution(n, m, x, y, queries):
    h = collections.deque(queries)
    xs, xe, ys, ye = x, x, y, y
    while h:
        dir, dist = h.pop()
        if dir == 0: # left -y
            if ys == 0:
                ye = min(m-1, ye+dist)
            else:
                if ys+dist > m-1: return 0
                ys = min(m-1, ys+dist)
                ye = min(m-1, ye+dist)
        elif dir == 1: # 우
            if ye == m-1:
                ys = max(0, ys-dist)
            else:
                if ye-dist < 0: return 0
                ys = max(0, ys-dist)
                ye = max(0, ye-dist)
        elif dir == 2: # 상
            if xs == 0:
                xe = min(n-1, xe+dist)
            else:
                if xs+dist > n-1: return 0
                xs = min(n-1, xs+dist)
                xe = min(n-1, xe+dist)
        elif dir == 3:  # 하
            if xe == n-1:
                xs = max(0, xs-dist)
            else:
                if xe-dist < 0: return 0
                xs = max(0, xs-dist)
                xe = max(0, xe-dist)
        if xe < xs or ye < ys:
            return 0
    return (xe-xs+1) * (ye-ys+1)
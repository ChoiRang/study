class Solution:
    def monkeyMove(self, n: int) -> int:
        max_int = 10 ** 9 + 7
        return (pow(2, n, max_int)-2) % max_int


"""
Testcase
3
4
5
6
7
8
9
10
100
996194169
500000003
-----
각 정점의 원숭이는 좌, 우 이동만 가능(2^n)
원숭이 -> 충돌 + 충돌X = 전체 이동갯수, 충돌하지 않는 경우는 전부 좌 또는 우측으로 이동했을 경우 -> 2^n - 2
pow(a, b, c) == a ^ b % c -> pow() 속도가 더 빠름
"""
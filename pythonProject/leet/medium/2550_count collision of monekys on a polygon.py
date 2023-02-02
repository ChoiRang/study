class Solution:
    def monkeyMove(self, n: int) -> int:
        max_int = 10 ** 9 + 7
        return (pow(2 , n, max_int)-2) % max_int


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
"""
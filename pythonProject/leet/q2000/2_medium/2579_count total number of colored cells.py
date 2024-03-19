class Solution:
    def coloredCells(self, n: int) -> int:
        # 1 5 13 25 41
        #   4  8 12 16
        #   4  12 24 40
        total = 1
        for i in range(1, n+1):
            total += 4 * (i-1)

        return total


# REF
class Solution2:
    def coloredCells(self, n: int) -> int:
        return 2 * n * (n-1) + 1

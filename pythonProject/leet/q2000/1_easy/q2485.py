class Solution:
    def pivotInteger(self, n: int) -> int:
        p = (n*(n+1) / 2) ** 0.5
        return int(p) if p.is_integer() else -1

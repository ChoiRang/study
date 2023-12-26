class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        left, right = 0, s.count("1")
        max_val = 0
        for i in range(n-1):
            if s[i] == "1":
                right -= 1
            else:
                left += 1
            max_val = max(max_val, left+right)

        return max_val
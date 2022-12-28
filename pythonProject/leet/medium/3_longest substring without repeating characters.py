class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used_ch = dict()
        start_point = 0
        max_length = 0
        for idx, ch in enumerate(s):
            if ch in used_ch and start_point <= used_ch[ch]:
                start_point = used_ch[ch] + 1
            else:
                max_length = max(max_length, idx-start_point+1)
            used_ch[ch] = idx

        return max_length

class Solution:
    def finalString(self, s: str) -> str:
        str1 = ""
        for ch in s:
            if ch == "i":
                str1 = str1[::-1]
            else:
                str1 += ch
        return str1
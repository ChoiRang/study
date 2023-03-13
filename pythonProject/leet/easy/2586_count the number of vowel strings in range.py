from typing import *


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowel = ['a', 'e', 'i', 'o', 'u']
        result = 0
        for i in range(left, right+1):
            word = words[i]
            if word[0] in vowel and word[-1] in vowel:
                result += 1

        return result

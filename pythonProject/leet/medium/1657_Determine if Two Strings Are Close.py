import collections


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        count1 = collections.Counter(word1)
        count2 = collections.Counter(word2)

        key1 = sorted(list(count1.keys()))
        key2 = sorted(list(count2.keys()))
        val1 = sorted(list(count1.values()))
        val2 = sorted(list(count2.values()))

        return val1 == val2 and key1 == key2

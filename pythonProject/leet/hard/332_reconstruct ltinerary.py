import collections
from typing import *


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        travel_dict = collections.defaultdict(list)
        result = []

        for start, end in sorted(tickets):
            travel_dict[start].append(end)

        def dfs(start):
            while travel_dict[start]:
                dfs(travel_dict[start].pop(0))
            result.append(start)

        dfs('JFK')
        return result[::-1]

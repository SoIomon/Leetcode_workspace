import collections
from typing import *


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(curr):
            while dict[curr]:
                tmp = dict[curr].pop(0)
                dfs(tmp)
            result.append(curr)

        dict = collections.defaultdict(list)
        for fro, to in tickets:
            dict[fro].append(to)
        for key in dict.keys():
            dict[key].sort()

        result = []
        dfs('JFK')

        return result[::-1]


a = Solution()
b = a.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])
print(b)

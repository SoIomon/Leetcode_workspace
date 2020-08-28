from typing import *
from collections import defaultdict

# class Solution:
#     def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
#         enable = [[False for i in range(n)] for i in range(n)]
#         graph = defaultdict(list)
#         for start, end in prerequisites:
#             graph[start].append(end)
#
#         for i in range(n):
#             queue = [i]
#             while queue:
#                 tmp = queue.pop(0)
#                 enable[i][tmp] = True
#                 for j in graph[tmp]:
#                     queue.append(j)
#
#         result = []
#         for query in queries:
#             result.append(enable[query[0]][query[1]])
#         return result

class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dp = [[False] * n for _ in range(n)]
        for p, c in prerequisites:
            dp[p][c] = True

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dp[i][k] and dp[k][j]:
                        dp[i][j] = True
        ans = []
        for i, j in queries:
            ans.append(dp[i][j])
        return ans


a = Solution().checkIfPrerequisite(n = 3, prerequisites = [[1,0],[2,0]], queries = [[0,1],[2,0]])
print(a)
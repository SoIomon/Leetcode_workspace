from Leetcode_type import *

class Solution:
    def sumOfDistancesInTree(self, N:int, edges: List[List[int]]) -> List[int]:
        ans = [0] * N
        sz = [0] * N
        dp = [0] * N
        graph = [[0] * N for _ in range(N)]

        def dfs(u: int, f: int):
            sz[u] = 1
            dp[u] = 0

            for i in range(N):
                if graph[u][i] and i != f:
                    dfs(i, u)
                    dp[u] += dp[i] + sz[i]
                    sz[u] += sz[i]

        def dfs2(u: int, f: int):
            ans[u] = dp[u]
            for i, _ in enumerate(graph[u]):
                if graph[u][i] and i != f:
                    pu = dp[u]
                    pv = dp[i]
                    su = sz[u]
                    sv = sz[i]

                    dp[u] -= dp[i] + sz[i]
                    sz[u] -= sz[i]
                    dp[i] += dp[u] + sz[u]
                    sz[i] += sz[u]

                    dfs2(i, u)
                    dp[u] = pu
                    dp[i] = pv
                    sz[u] = su
                    sz[i] = sv

        for edge in edges:
            u, v = edge[0], edge[1]
            graph[u][v] = 1
            graph[v][u] = 1

        dfs(0, -1)
        dfs2(0, -1)
        return ans

print(Solution().sumOfDistancesInTree(N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]))

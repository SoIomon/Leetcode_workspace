from Leetcode_type import *

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        cost = [[0]*m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                if i != j:
                    cost[i][j] = abs(points[i][0] - points[j][0])+abs(points[i][1] - points[j][1])
                else:
                    cost[i][j] = 0
        res = 0
        lowcost = [0] * m  # 最小代价数组

        # 初始化lowcost
        for i in range(m): lowcost[i] = cost[0][i]
        # 最小生成树构建m-1条边
        for i in range(1,m):
            min=0x3f3f3f
            index=0
            for j,data in enumerate(lowcost):
                if data < min and data != 0:
                    min=data
                    index=j
            res+=min
            lowcost[index]=0
            for j in range(m):
                if cost[index][j] < lowcost[j]:
                    lowcost[j]=cost[index][j]
        return res 

print(Solution().minCostConnectPoints(points = [[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(Solution().minCostConnectPoints(points = [[3,12],[-2,5],[-4,1]]))
print(Solution().minCostConnectPoints(points = [[0,0],[1,1],[1,0],[-1,1]]))
print(Solution().minCostConnectPoints(points = [[-1000000,-1000000],[1000000,1000000]]))
print(Solution().minCostConnectPoints(points = [[0,0]]))
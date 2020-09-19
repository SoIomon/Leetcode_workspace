from Leetcode_type import *


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [False] * len(arr)
        queue = [start]
        while queue:
            pos = queue.pop(0)
            visited[pos] = True
            if 0 <= pos + arr[pos] < len(arr) and not visited[pos + arr[pos]]:
                queue.append(pos + arr[pos])
            if 0 <= pos - arr[pos] < len(arr) and not visited[pos - arr[pos]]:
                queue.append(pos - arr[pos])
        for i, v in enumerate(arr):
            if v == 0 and visited[i]:
                return True
        return False

print(Solution().canReach(arr = [4,2,3,0,3,1,2], start = 5))
print(Solution().canReach(arr = [4,2,3,0,3,1,2], start = 0))
print(Solution().canReach(arr = [3,0,2,1,2], start = 2))
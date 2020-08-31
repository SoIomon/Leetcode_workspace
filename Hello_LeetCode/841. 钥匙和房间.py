from typing import *


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True

        queue = rooms[0]
        while queue:
            key = queue.pop(0)
            if visited[key] == False:
                for i in rooms[key]:
                    queue.append(i)
                visited[key] = True
        return all(visited)


a = Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]])
print(a)

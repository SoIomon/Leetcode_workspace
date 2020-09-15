from Leetcode_type import *


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        return min(sum(distance[start:destination]), sum(distance) - sum(distance[start:destination]))


print(Solution().distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 1))
print(Solution().distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 2))
print(Solution().distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 3))
print(Solution().distanceBetweenBusStops(distance = [1,2,3,4], start = 3, destination = 0))

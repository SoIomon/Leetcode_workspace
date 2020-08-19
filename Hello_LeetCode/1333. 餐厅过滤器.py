from typing import *


class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> \
            List[int]:
        def is_veganFriendly(rest):
            if veganFriendly == 1:
                return rest[2] == 1
            else:
                return 1

        def is_less_maxPrice(rest):
            return rest[3] <= maxPrice

        def is_less_maxDistance(rest):
            return rest[4] <= maxDistance

        restaurants = list(filter(is_veganFriendly, restaurants))
        restaurants = list(filter(is_less_maxPrice, restaurants))
        restaurants = list(filter(is_less_maxDistance, restaurants))

        return [i[0] for i in sorted(restaurants, key=lambda x:(x[1],x[0]), reverse=True)]


restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]]
veganFriendly = 1
maxPrice = 50
maxDistance = 10

a = Solution()
b = a.filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance)
print(b)

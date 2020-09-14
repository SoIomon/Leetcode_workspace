from Leetcode_type import *


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pairs_map = {}
        res = 0
        for pair in pairs:
            pairs_map[pair[0]] = pair
            pairs_map[pair[1]] = pair

        def get_preference(i, j):
            return preferences[i].index(j)

        for i in range(n):
            flag = False
            now_pair = sum(pairs_map[i]) - i
            now_preference = get_preference(i, now_pair)
            for j in range(n):
                if j != i and j != now_pair and get_preference(i,j) < now_preference:
                    tmp_pair = sum(pairs_map[j]) - j
                    if get_preference(j, tmp_pair) > get_preference(j, i):
                        flag = True
            if flag:
                res += 1
        return res

print(Solution().unhappyFriends(n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]]))
print(Solution().unhappyFriends(n = 2, preferences = [[1], [0]], pairs = [[1, 0]]
))
print(Solution().unhappyFriends(n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]
))
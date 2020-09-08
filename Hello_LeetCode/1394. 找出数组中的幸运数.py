from Leetcode_type import *

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dict = collections.defaultdict(int)
        for i in arr:
            dict[i] += 1
        result = []
        for key in dict.keys():
            result.append((key, dict[key]))
        result.sort(key=lambda x: x[0], reverse=True)
        for i in result:
            if i[0] == i[1]:
                return i[0]
        return -1

print(Solution().findLucky(arr = [1,2,2,3,3,3]))
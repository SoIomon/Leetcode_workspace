from Leetcode_type import *

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        if len(s) == 1:
            return 0
        pattern = []
        result = 0

        i, j = 0, 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            if i != j-1:
                pattern.append((i, j - 1))
            i = j

        for p in pattern:
            tmp = cost[p[0]:p[1]+1]
            result += sum(tmp) - max(tmp)

        return result


print(Solution().minCost(s = "aa", cost = [1,2]))


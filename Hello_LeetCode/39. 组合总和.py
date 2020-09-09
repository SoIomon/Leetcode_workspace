from Leetcode_type import *

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        for i, v in enumerate(candidates):
            if target - v > 0:
                for j in self.combinationSum(candidates, target - v):
                    if j[0] >= v:
                        ans.append([v] + j)
            if target - v == 0:
                ans.append([v])
            if target - v < 0:
                break
        return ans


print(Solution().combinationSum(candidates = [2,3,6,7], target = 7))
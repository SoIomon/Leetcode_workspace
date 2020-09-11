from Leetcode_type import *


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        for i, v in enumerate(candidates):
            if target - v > 0:
                for j in self.combinationSum2(candidates[i + 1:], target - v):
                    ans.append([v] + j)
            if target - v == 0:
                ans.append([v])

        res = []
        for i in ans:
            if i not in res:
                res.append(i)

        return


print(Solution().combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))

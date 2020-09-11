from Leetcode_type import *

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = collections.defaultdict(int)
        for c in text:
            count[c] += 1
        tmp = [count[i] for i in 'balon']
        tmp[2] = tmp[2] // 2
        tmp[3] = tmp[3] // 2
        return min(tmp)


print(Solution().maxNumberOfBalloons('leet'))
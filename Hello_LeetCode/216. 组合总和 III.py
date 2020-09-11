from Leetcode_type import *

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        if k > 9 or n > (19 - k) * k / 2:
            return []
        if k == 9:
            return [[i for i in range(1,10)]] if n == 45 else []
        if k == 1 and 1 <= n <= 9:
            return [[n]]
        for i in range(1, 10)[::-1]:
            if n - i > 0:
                for j in self.combinationSum3(k-1, n-i):
                    if j[-1] < i:
                        ans.append(j + [i])
        return ans

print(Solution().combinationSum3(9, 45))
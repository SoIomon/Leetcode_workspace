from Leetcode_type import *

class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        used = collections.Counter(A)
        for x in sorted(A, key=abs):
            if used[x] == 0:
                continue
            if used[2*x] == 0:
                return False
            used[x] -= 1
            used[2*x] -= 1
        return True


print(Solution().canReorderDoubled([3,1,3,6]))
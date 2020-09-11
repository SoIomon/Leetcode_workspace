from Leetcode_type import *

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        N = len(A)
        floor = N
        for i in range(N-1, -1, -1):
            floor = min(floor, A[i])
            if i >= 2 and A[i-2] > floor:
                return False
        return True


print(Solution().isIdealPermutation( A = [1,2,0]))
from Leetcode_type import *


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        judge = [1] + [1 if arr[i-1] <= arr[i] else 0 for i in range(1, len(arr))]
        if 0 not in judge:
            return 0
        i, j = judge.index(1)


print(Solution().findLengthOfShortestSubarray(arr = [5,4,3,2,1]))
print(Solution().findLengthOfShortestSubarray(arr = [1,2,3,10,4,2,3,5]))
print(Solution().findLengthOfShortestSubarray(arr = [1,2,3]))
print(Solution().findLengthOfShortestSubarray(arr = [1]))
from Leetcode_type import *

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        plus_count = 0
        max_multi_count = 0
        for i in nums:
            binval = bin(i)
            length = len(binval) - 2
            plus_count += binval.count("1")
            if length > 1:
                multi_count = length - 1
                max_multi_count = max(multi_count, max_multi_count)
        return plus_count + max_multi_count


print(Solution().minOperations([1, 5]))
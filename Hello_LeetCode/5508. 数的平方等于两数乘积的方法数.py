from Leetcode_type import *
import collections

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        nums1_pow = [i * i for i in nums1]
        nums2_pow = [i * i for i in nums2]
        set1 = collections.defaultdict(int)
        set2 = collections.defaultdict(int)

        for i in range(len(nums1)):
            for j in range(i+1, len(nums1)):
                set1[nums1[i] * nums1[j]] += 1

        for i in range(len(nums2)):
            for j in range(i+1, len(nums2)):
                set2[nums2[i] * nums2[j]] += 1

        for i in nums1_pow:
            result += set2[i]

        for i in nums2_pow:
            result += set1[i]

        return result


print(Solution().numTriplets(nums1 = [4,7,9,11,23], nums2 = [3,5,1024,12,18]))

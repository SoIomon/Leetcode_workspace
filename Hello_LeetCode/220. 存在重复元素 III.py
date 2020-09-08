from Leetcode_type import *

# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
#         for i, v in enumerate(nums):
#             for j in range(i+1,i+k+1):
#                 if j < len(nums):
#                     if abs(v-nums[j]) <= t:
#                         return True
#         return False

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucket_map = collections.defaultdict(list)
        for i, v in enumerate(nums):
            bucket_ID = v // (t + 1)
            if bucket_map[bucket_ID]:
                return True
            if bucket_map[bucket_ID - 1] and abs(bucket_map[bucket_ID-1][0] - v) <= t:
                return True
            if bucket_map[bucket_ID + 1] and abs(bucket_map[bucket_ID+1][0] - v) <= t:
                return True
            bucket_map[bucket_ID].append(v)
            if i >= k:
                remove_ID = nums[i-k] // (t + 1)
                bucket_map[remove_ID].pop()
        return False

print(Solution().containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], k = 2, t = 3))
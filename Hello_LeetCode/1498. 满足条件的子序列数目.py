from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        if nums[0] * 2 > target:
            return 0

        left = 0
        right = len(nums) - 1
        res = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                res += 2 ** (right - left)
                left += 1
            else:
                right -= 1
        return res % (10 ** 9 + 7)

if __name__ == '__main__':
    a = Solution()
    b = a.numSubseq([3,3,6,8], target=10)
    print(b)
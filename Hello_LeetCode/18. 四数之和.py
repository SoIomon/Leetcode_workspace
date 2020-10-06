from Leetcode_type import *


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []

        def Search(i, target, oneSolution):

            if target == 0 and len(oneSolution) == 4:  # 出口，找到正确的解了
                output.append(oneSolution)
                return
            elif len(oneSolution) > 4 or i >= len(nums):  # 剪枝，超范围了
                return

            if target - nums[i] - (3 - len(oneSolution)) * nums[-1] > 0:  # 当前这个数太小了
                Search(i + 1, target, oneSolution)
            elif target - (4 - len(oneSolution)) * nums[i] < 0:  # 当前组数的和太大了
                return
            else:  # 当前组数似乎没毛病
                Search(i + 1, target, oneSolution)  # 不选这个数
                Search(i + 1, target - nums[i], oneSolution + [nums[i]])  # 选这个数

        Search(0, target, [])

        output1 = []
        output2 = []
        for t in output:
            if set(t) not in output1:
                output1.append(set(t))
                output2.append(t)

        return output2



print(Solution().fourSum(nums = [1, 0, -1, 0, -2, 2],target = 0))

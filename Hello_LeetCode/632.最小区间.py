from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        if k == 1:
            return [nums[0][0], nums[0][0]]

        # init
        index_list = [0] * k
        value_list = [nums[i][index_list[i]] for i in range(k)]
        start, end = -1e5, 1e5

        while True:
            t_start, t_end = min(value_list), max(value_list)
            t_pos = value_list.index(t_start)
            if t_end - t_start < end - start:
                start, end = t_start, t_end
            index_list[t_pos] += 1
            if index_list[t_pos] < len(nums[t_pos]):
                value_list[t_pos] = nums[t_pos][index_list[t_pos]]
            else:
                break
        return [start, end]


if __name__ == '__main__':
    a = Solution()
    print(a.smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]))
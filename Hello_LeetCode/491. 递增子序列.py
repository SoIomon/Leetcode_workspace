from typing import *

"""
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        queue = [[v, i] for i, v in enumerate(nums)]
        result = set()

        while queue:
            print(queue)
            tmp = queue.pop(0)
            tmp, i = tmp[:-1], tmp[-1]

            if i == len(nums) - 1:
                if len(tmp) >= 2:
                    result.add(tuple(tmp))
            else:
                for j in range(i+1, len(nums)):
                    tmp_add = [i for i in tmp]
                    tmp_nadd = [i for i in tmp]

                    tmp_nadd.append(j)
                    queue.append(tmp_nadd)

                    if nums[j] >= tmp_add[-1]:
                        tmp_add.append(nums[j])
                        tmp_add.append(j)
                        queue.append(tmp_add)

        return [list(i) for i in result]
"""

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        pres = {(nums[0], )}
        for i in nums[1:]:
            print(pres)
            pres.update({j+(i, ) for j in pres if j[-1] <= i})
            pres.add((i, ))
        return list([list(i) for i in pres if len(i) > 1])



a = Solution()
b = a.findSubsequences([1,2,3,4,5])

print(b)

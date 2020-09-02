from Leetcode_type import *

class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        Sum1, Sum2 = sum(array1), sum(array2)
        if (Sum1 - Sum2) & 1:
            return []
        else:
            tmp = (Sum1-Sum2)//2
            seta = set(array1)
            setb = set(array2)
            for a in seta:
                b = a - tmp
                if b in setb:
                    return [a, b]
        return []


array1 = [1,2,3]
array2 = [4,5,6]
print(Solution().findSwapValues(array1, array2))

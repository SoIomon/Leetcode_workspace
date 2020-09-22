from Leetcode_type import *


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count_dict = collections.defaultdict(int)
        for line in matrix:
            tmp = line
            if line[0] == 1:
                tmp = [1-i for i in line]
            key = tuple(tmp)
            count_dict[key] += 1

        ans = [count_dict[key] for key in count_dict.keys()]
        return max(ans)

print(Solution().maxEqualRowsAfterFlips([[0, 1], [1, 1]]))
print(Solution().maxEqualRowsAfterFlips([[0, 1], [1, 0]]))
print(Solution().maxEqualRowsAfterFlips([[0, 0, 0], [0, 0, 1], [1, 1, 0]]))

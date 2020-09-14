from Leetcode_type import *

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    tmp_i = sum(mat[i])
                    tmp_j = sum([mat[k][j] for k in range(m)])
                    if tmp_i + tmp_j == 2:
                        res += 1
        return res

print(Solution().numSpecial([[1,0,0],
            [0,0,1],
            [1,0,0]]))
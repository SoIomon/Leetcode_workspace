from Leetcode_type import *

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        result = 0
        for i in range(n):
            j = n - 1 - i
            result += mat[i][i] + mat[i][j] if i != j else mat[i][i]
        return result
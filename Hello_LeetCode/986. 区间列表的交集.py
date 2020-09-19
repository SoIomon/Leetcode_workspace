from Leetcode_type import *

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        ans = []
        while i < len(A) and j < len(B):
            si, ei = A[i]
            sj, ej = B[j]
            if si > ej:
                j += 1
            elif ei < sj:
                i += 1
            else:
                s = max(si, sj)
                e = min(ei, ej)
                ans.append([s, e])
                if ei <= ej:
                    i += 1
                else:
                    j += 1
        return ans
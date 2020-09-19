from Leetcode_type import *


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        tmp = sum([i if i % 2 == 0 else 0  for i in A])
        for query in queries:
            old_val = A[query[1]]
            new_val = old_val + query[0]
            A[query[1]] = new_val
            if old_val % 2 == 0:
                tmp -= old_val
            if new_val % 2 == 0:
                tmp += new_val
            ans.append(tmp)
        return ans

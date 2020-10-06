from Leetcode_type import *

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J_map = collections.defaultdict(int)
        for i in J:
            J_map[i] += 1

        ans = 0
        for i in S:
            ans += J_map[i]
        return ans
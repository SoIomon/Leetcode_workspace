from Leetcode_type import *

class Solution:
    def firstUniqChar(self, s: str) -> str:
        frequency = collections.defaultdict(int)
        for i in s:
            frequency[i] += 1
        for i in s:
            if frequency[i] == 1:
                return i
        return ' '


print(Solution().firstUniqChar("abaccdeff"))
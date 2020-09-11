from Leetcode_type import *


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        s = []
        result = 0
        for i in nums:
            if i == 0:
                s.append('0')
            elif i > 0:
                s.append('p')
            else:
                s.append('n')
        s = ''.join(s)
        s = s.split('0')
        for i in s:
            cp, cn = i.count('p'), i.count('n')
            if cn % 2 == 0:
                result = result if result > cp + cn else cn + cp
            else:
                r = len(i) - i.rfind('n')
                l = i.find('n') + 1
                aaa = min(r, l)
                result = result if result > len(i) - aaa else len(i) - aaa
        return result


print(Solution().getMaxLen(nums = [9,10,1,0,19,20,-28,30,-12,20,11,-8,7,21,-26]))

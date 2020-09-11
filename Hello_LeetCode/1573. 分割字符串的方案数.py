from Leetcode_type import *

class Solution:
    def numWays(self, s: str) -> int:
        epo: int = 1000000007
        result = 0

        count = s.count('1')
        if count % 3 != 0:
            return 0
        else:
            count = count // 3
            if count == 0:
                n = len(s) - 2
                result = n * (n + 1) // 2
            else:
                cc = 0
                f1, f2 = 0, 0
                for i, v in enumerate(s):
                    if v == '1':
                        cc += 1
                    if cc == count:
                        f1 += 1
                    if cc == count * 2:
                        f2 += 1
                result = f1 * f2
        return result % epo


print(Solution().numWays('00000000'))

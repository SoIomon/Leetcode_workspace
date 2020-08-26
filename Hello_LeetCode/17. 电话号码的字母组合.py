from typing import *

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        n = len(digits)
        digits = [i for i in digits]
        ans = ['']
        if n == 0:
            return []
        while digits:
            now_d = digits.pop(0)
            if now_d in dict:
                tmp = []
                for i in dict[now_d]:
                    for j in ans:
                        tmp.append(j+i)
                ans = tmp
        return ans


a = Solution()
b = a.letterCombinations('')
print(b)
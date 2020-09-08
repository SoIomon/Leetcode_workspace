from Leetcode_type import *


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        ans = []
        window = [0 for _ in range(26)]
        pattern = [0 for _ in range(26)]
        window_size = len(p)

        for i in range(len(p)):
            pattern[ord(p[i]) - 97] += 1
            window[ord(s[i]) - 97] += 1

        left, right = 0, window_size - 1
        while right < len(s) - 1:
            if window == pattern:
                ans.append(left)
            window[ord(s[left]) - 97] -= 1
            window[ord(s[right + 1]) - 97] += 1
            left, right = left + 1, right + 1
        if window == pattern:
            ans.append(left)

        return ans


print(Solution().findAnagrams("cbaebabacd", "abc"))

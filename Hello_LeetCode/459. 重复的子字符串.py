class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        max_len = len(s) // 2
        tmp_len = 1

        while tmp_len <= max_len:
            k = len(s) // tmp_len
            if len(s) % tmp_len == 0:
                tmp_result = True
                for i in range(1, k):
                    tmp_result = tmp_result and (s[tmp_len * i:tmp_len * i + tmp_len] == s[:tmp_len])
                if tmp_result:
                    return True
            tmp_len += 1

        return False


a = Solution()
b = a.repeatedSubstringPattern('ababab')
print(b)

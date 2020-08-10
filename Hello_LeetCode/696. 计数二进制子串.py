class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        length = len(s)
        cur = 1
        prev = 0
        res = 0
        for i in range(1, length):
            if s[i] == s[i-1]:
                cur += 1
            else:
                res += min(cur, prev)
                prev = cur
                cur = 1
        return res + min(cur, prev)


if __name__ == '__main__':
    a = Solution()
    b = a.countBinarySubstrings('00110011')
    print(b)
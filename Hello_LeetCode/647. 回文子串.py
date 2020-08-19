def count_P(s, center_left, center_right):
    p, q = center_left, center_right
    count = 0
    while 0 <= p < len(s) and 0 <= q < len(s) and s[p] == s[q]:
        count += 1
        p -= 1
        q += 1
    # print(count, center_left, center_right)
    return count


class Solution:

    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            result += count_P(s, i, i)
            result += count_P(s, i, i + 1)
        return result


a = Solution()
b = a.countSubstrings('abc')
print(b)

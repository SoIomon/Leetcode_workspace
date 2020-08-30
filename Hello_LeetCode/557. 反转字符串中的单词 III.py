class Solution:
    def reverseWords(self, s: str) -> str:
        tmp = s.split(' ')
        tmp = [word[::-1] for word in tmp]
        return ' '.join(tmp)


a = Solution().reverseWords("Let's take LeetCode contest")
print(a)
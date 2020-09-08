class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [s[0]]
        count_s = [1]
        for i in range(1, len(s)):
            if stack and s[i] == stack[-1]:
                count_s[-1] += 1
            else:
                stack.append(s[i])
                count_s.append(1)
            if count_s[-1] == k:
                stack.pop(-1)
                count_s.pop(-1)
        return ''.join([stack[i] * count_s[i] for i in range(len(stack))])





print(Solution().removeDuplicates("yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", 4))
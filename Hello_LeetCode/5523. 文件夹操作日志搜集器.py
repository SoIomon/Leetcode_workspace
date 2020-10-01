from Leetcode_type import *

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == '../':
                if stack:
                    stack.pop(-1)
            elif log == './':
                pass
            else:
                stack.append(1)
        return len(stack)
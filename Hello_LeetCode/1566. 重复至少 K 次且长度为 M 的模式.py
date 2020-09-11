from Leetcode_type import *

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr)-m):
            window_key = arr[i:i+m] * k
            print(window_key)
            for j in range(len(arr) - len(window_key)+1):
                if arr[j:j + len(window_key)] == window_key:
                    return True
        return False


print(Solution().containsPattern(arr = [1,2,4,4,4,4], m = 1, k = 3))
print(Solution().containsPattern(arr = [2,2,2,2], m = 2, k = 3))
print(Solution().containsPattern(arr = [2,2], m = 1, k = 2))
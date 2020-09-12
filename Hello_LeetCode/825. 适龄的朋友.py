from Leetcode_type import *

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = collections.defaultdict(int)

        for age in ages:
            count[age] += 1

        result = 0
        nages = [key for key in count.keys()]
        nages.sort()

        def can_send(A: int, B: int)->bool:
            if nages[B] <= 0.5 * nages[A] + 7:
                return False
            if nages[B] > nages[A]:
                return False
            if nages[B] > 100 > nages[A]:
                return False
            return True

        for i in range(len(nages)):
            for j in range(0, i+1):
                if i != j:
                    if can_send(i, j):
                        result += count[nages[i]] * count[nages[j]]
                else:
                    if can_send(i, i):
                        result += count[nages[i]] * (count[nages[i]] - 1)

        return result


print(Solution().numFriendRequests([16,16, 16]))
print(Solution().numFriendRequests([16,17,18]))
print(Solution().numFriendRequests([20,30,100,110,120]))
print(Solution().numFriendRequests([73,106,39,6,26,15,30,100,71,35,46,112,6,60,110]))
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        direction = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
        postion = [0, 0]
        for step in moves:
            dx, dy = direction[step]
            postion[0] += dx
            postion[1] += dy
        return postion == [0, 0]

a = Solution()
b = a.judgeCircle('LL')
print(b)
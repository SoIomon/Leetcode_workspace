import bisect


class ExamRoom:

    def __init__(self, N: int):
        self.l = []
        self.N = N

    def seat(self) -> int:
        if len(self.l) == 0:
            self.l.append(0)
            return 0
        ret = 0
        mx = 0
        for i in range(1, len(self.l)):
            if (self.l[i] - self.l[i - 1]) // 2 > mx:
                mx = (self.l[i] - self.l[i - 1]) // 2
                ret = (self.l[i] + self.l[i - 1]) // 2
        if self.l[0] >= mx:
            ret = 0
            mx = self.l[0]
        if self.N - self.l[-1] - 1 > mx:
            ret = self.N - 1
        bisect.insort(self.l, ret)
        return ret

    def leave(self, p: int) -> None:
        self.l.remove(p)



examroom = ExamRoom(10)
examroom.seat()
examroom.seat()
examroom.seat()
examroom.seat()
examroom.leave(4)
examroom.seat()
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        S = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        C = 2 * (3 - (year // 100) % 4)
        Y = ((year % 100) % 28 + ((year % 100) % 28) // 4) % 7
        M = int((3.4 + (month - 3) % 12 * 2.6) % 7)
        D = int(day % 7)
        if year % 4 == 0 and (month == 1 or month == 2):
            Y = Y - 1
        if month == 1 or month == 2:
            M = M - 1
        f = (C + Y + M + D) % 7
        return S[f]
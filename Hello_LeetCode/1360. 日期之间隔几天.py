from datetime import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1 = datetime.strptime(date1,'%Y-%m-%d')
        date2 = datetime.strptime(date2,'%Y-%m-%d')
        res = abs((date1 - date2).days)
        return res

a = Solution().daysBetweenDates(date1 = "2019-06-29", date2 = "2019-06-30")
print(a)
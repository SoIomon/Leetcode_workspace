class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = version1.split('.')
        l2 = version2.split('.')

        l1 = [int(i) for i in l1]
        l2 = [int(i) for i in l2]

        i = 0
        while i < len(l1) or i < len(l2):
            t1 = l1[i] if i < len(l1) else 0
            t2 = l2[i] if i < len(l2) else 0

            if t1 > t2:
                return 1
            if t1 < t2:
                return -1
            i += 1

        return 0

print(Solution().compareVersion(version1 = "1.01", version2 = "1.001"))
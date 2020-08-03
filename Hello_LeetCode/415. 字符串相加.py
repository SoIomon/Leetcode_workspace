class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ''
        num1, num2 = num1[::-1], num2[::-1]
        i, j = 0, 0
        c = 0
        while i < len(num1) or j < len(num2) or c != 0:
            a = ord(num1[i]) - ord('0') if i < len(num1) else 0
            b = ord(num2[j]) - ord('0') if j < len(num2) else 0
            tmp = a + b + c
            c = tmp // 10
            result += chr(tmp % 10 + ord('0'))
            i, j = i+1, j+1
        return result[::-1]


if __name__ == '__main__':
    a = Solution()
    b = a.addStrings('1', '9')
    print(b)

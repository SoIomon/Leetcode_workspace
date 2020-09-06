class Solution:
    def modifyString(self, s: str) -> str:
        result = []
        char_list = [chr(i) for i in range(97, 97+26)]

        def getonechar(a, b):
            tmp = [i for i in char_list if i != a and i != b]
            return tmp[0]

        for i, char in enumerate(s):
            if char == '?':
                before = ' '
                after = ' '
                if i > 0:
                    before = result[i-1]
                if i < len(s) - 1:
                    after = s[i+1]
                result.append(getonechar(before, after))
            else:
                result.append(char)
        return ''.join(result)


print(Solution().modifyString("j?qg??b"))
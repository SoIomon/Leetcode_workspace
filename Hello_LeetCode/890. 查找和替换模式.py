from Leetcode_type import *

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def change2int(word: str) -> list:
            ans = []
            count = 0
            count_dict = {}
            for s in word:
                if s in count_dict.keys():
                    ans.append(count_dict[s])
                else:
                    count_dict[s] = count
                    ans.append(count)
                    count += 1
            return ans

        pattern_list = change2int(pattern)
        res = []
        for word in words:
            if pattern_list == change2int(word):
                res.append(word)
        return res

print(Solution().findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"))
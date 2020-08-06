from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = set()
        n = len(words)
        lookup_dict = {words[i][::-1]:i for i in range(n)}

        for i, word in enumerate(words):
            for m in range(len(word) + 1):
                if word[:m] == word[:m][::-1]:
                    if word[m:] in lookup_dict.keys():
                        result.add((lookup_dict[word[m:]], i))
                if word[m:] == word[m:][::-1]:
                    if word[:m] in lookup_dict.keys():
                        result.add((i,lookup_dict[word[:m]]))

        return [i for i in result if i[0] != i[1]]


if __name__ == '__main__':
    a = Solution()
    b = a.palindromePairs(["abcd","dcba","lls","s","sssll"])
    print(b)
class Solution:
    def reorderSpaces(self, text: str) -> str:
        count_space = 0
        text_list = text.split()
        for s in text:
            if s == ' ':
                count_space += 1
        count_word = len(text_list)

        if count_word == 1:
            return text_list[0] + ' ' * count_space
        else:
            gap_length = count_space // (count_word - 1)
            tail_length = count_space % (count_word - 1)
            return (' ' * gap_length).join(text_list) + ' ' * tail_length


print(Solution().reorderSpaces(text = "  this   is  a sentence "))
print(Solution().reorderSpaces(text = " practice   makes   perfect"))
print(Solution().reorderSpaces(text = "hello   world"))
print(Solution().reorderSpaces(text = "  walks  udp package   into  bar a"))
print(Solution().reorderSpaces(text = "a"))

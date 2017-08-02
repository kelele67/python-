# def FirstAppearingOnce(str):
#     new_str = ''
#     for i in range(1, len(str)+1):
#         count = 0
#         for s in str[:i]:
#             if str[:i].count(s) == 1:
#                 new_str = new_str + s
#                 break
#             else:
#                 if count == i-1:
#                     new_str = new_str + '#'
#                     break
#                 else:
#                     count = count + 1
#     print new_str

# str = raw_input()
# FirstAppearingOnce(str)

class Solution:
    def __init__(self):
        self.chars = ''
        self.dic = {}

    def FirstAppearingOnce(self):
        for char in self.chars:
            if self.dic[char] == 1:
                return char
        return '#'

    def Insert(self, char):
        if self.dic.get(char):
            self.dic[char] += 1
        else:
            self.dic[char] = 1
        self.chars += char
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = s.lstrip().strip()
        tmp = s.split(' ')
        tmp = [item for item in tmp if item <> '']
        tmp = tmp[::-1]
        if s <> "":
            return " ".join(tmp)
        else:
            return ""

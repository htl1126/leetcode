class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.lstrip().strip()
        tmp = s.split(' ')
        tmp = [item for item in tmp if item != '']
        tmp = tmp[::-1]
        if s != "":
            return " ".join(tmp)
        else:
            return ""

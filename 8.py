# ad-hoc

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0: return 0
        str = list(str.strip())
        sign = -1 if str[0] == '-' else 1
        if str[0] in ['+', '-']: del str[0]
        ans, i = 0, 0
        while i < len(str) and str[i].isdigit():
            ans = ans * 10 + ord(str[i]) - ord('0')
            i += 1
        return max(-2 ** 31, min(sign * ans, 2 ** 31 - 1))

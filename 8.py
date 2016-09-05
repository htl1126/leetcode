# ad-hoc


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        str = list(str.strip())
        sign = [1, -1][str[0] == '-']
        if str[0] in '-+':
            del str[0]
        ans, i = 0, 0
        while i < len(str) and '0' <= str[i] <= '9':
            ans = ans * 10 + ord(str[i]) - ord('0')
            i += 1
        return min(2 ** 31 - 1, max(ans * sign, - 2 ** 31))

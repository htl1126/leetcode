class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ''
        values = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                  90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V',
                  4: 'IV', 1: 'I'}
        sorted_keys = sorted(values.keys(), reverse=True)
        for key in sorted_keys:
            while num >= key:
                ans += values[key]
                num -= key
        return ans

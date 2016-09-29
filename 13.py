class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        addmap = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5,
                  'I': 1}
        submap = {'CM': 200, 'CD': 200, 'XL': 20, 'XC': 20, 'IV': 2, 'IX': 2}
        ans = 0
        for c in s:
            ans += addmap[c]
        for sub_symb in submap:
            if sub_symb in s:
                ans -= submap[sub_symb]
        return ans

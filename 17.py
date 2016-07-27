class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'0': ' ', '1': '*', '2': 'abc', '3': 'def', '4': 'ghi',
               '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ans = []
        if digits == '':
            return []

        def get_comb(digits, res):
            if digits == '':
                ans.append(res)
            else:
                for c in dic[digits[0]]:
                    get_comb(digits[1:], res + c)
        get_comb(digits, '')
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.letterCombinations('23')

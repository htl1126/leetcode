class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'0': ' ', '1': '*', '2': 'abc', '3': 'def', '4': 'ghi',
               '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits:
            return []
        if len(digits) == 1:
            return list(dic[digits])
        ans = []
        for s in self.letterCombinations(digits[1:]):
            for c in dic[digits[0]]:
                ans.append(c + s)
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.letterCombinations('23')

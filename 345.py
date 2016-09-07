class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l, r, s = 0, len(s) - 1, list(s)
        while l < r:
            if s[l] not in 'aeiouAEIOU':
                l += 1
            elif s[r] not in 'aeiouAEIOU':
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]
                l, r = l + 1, r - 1
        return ''.join(s)

if __name__ == '__main__':
    sol = Solution()
    print sol.reverseVowels('xyz')

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ''
        n -= 1
        alphabet = [chr(ord('A') + i) for i in xrange(26)]
        while n >= 0:
            ans += alphabet[n % 26]
            n = n / 26 - 1
        return ans[::-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.convertToTitle(1)

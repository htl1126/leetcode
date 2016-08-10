import sys


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = [int(i) for i in num1][::-1]
        num2 = [int(i) for i in num2][::-1]
        len1, len2 = len(num1), len(num2)
        ans = [0 for _ in xrange(len1 + len2)]
        for i in xrange(len1):
            for j in xrange(len2):
                ans[i + j] += num1[i] * num2[j]
        for i in xrange(len(ans) - 1):
            ans[i + 1] += ans[i] / 10
            ans[i] %= 10
        for i in xrange(len(ans) - 1, -1, -1):
            if ans[i] != 0:
                return ''.join([str(i) for i in reversed(ans[:i + 1])])
        return '0'

if __name__ == '__main__':
    sol = Solution()
    print sol.multiply(sys.argv[1], sys.argv[2])

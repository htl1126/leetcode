# faster solution: https://leetcode.com/discuss/49026/share-my-60-ms-python-solution

import sys

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        atoi = lambda c: ord(c) - ord('0')
        num1 = num1[::-1]
        num2 = num2[::-1]
        ans = [0] * (len(num1) + len(num2))
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                product = atoi(num1[i]) * atoi(num2[j])
                ans[i + j] += product
        ans.append(0)
        for i in xrange(1, len(ans)):
            ans[i] += ans[i - 1] / 10
            ans[i - 1] %= 10
        ans = ans[::-1]
        for i in xrange(len(ans)):
            if ans[i] != 0:
                return ''.join([str(item) for item in ans[i:]])
        return '0'
        
if __name__ == '__main__':
    sol = Solution()
    print sol.multiply(sys.argv[1], sys.argv[2])

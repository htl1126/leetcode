import sys

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a[::-1]
        b = b[::-1]
        if len(a) < len(b):
            a, b = b, a
        b = '{0}{1}'.format(b, '0' * (len(a) - len(b)))
        ans = ''
        atoi = lambda c: ord(c) - ord('0')
        carry = 0
        for i in xrange(len(a)):
            curr_digit = atoi(a[i]) + atoi(b[i]) + carry
            if curr_digit > 1:
                curr_digit -= 2
                carry = 1
            else:
                carry = 0
            ans = '{0}{1}'.format(ans, curr_digit)
        if carry == 1:
            ans = '{0}{1}'.format(ans, 1)
        return ans[::-1]
        
if __name__ == '__main__':
    sol = Solution()
    print sol.addBinary(sys.argv[1], sys.argv[2])

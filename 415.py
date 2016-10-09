class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        num1, num2 = num1[::-1], num2[::-1]
        ans, carry = [0] * len(num1), 0
        for i in xrange(len(num1)):
            ans[i] += int(num1[i]) + carry
            if i < len(num2):
                ans[i] += int(num2[i])
            carry = ans[i] > 9
            ans[i] -= carry * 10
        if carry:
            ans.append(1)
        return ''.join(str(i) for i in ans[::-1]) or '0'

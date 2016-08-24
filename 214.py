# ref: https://discuss.leetcode.com/topic/14607/python-solution-kmp


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        A = s + '*' + s[::-1]
        cont = [0]
        for i in xrange(1, len(A)):  # Constructing the failure function
            index = cont[i - 1]
            while index > 0 and A[index] != A[i]:
                index = cont[index - 1]
            cont.append(index + (A[index] == A[i]))
        return s[cont[-1]:][::-1] + s

if __name__ == '__main__':
    sol = Solution()
    print sol.shortestPalindrome('aace')

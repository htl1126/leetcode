# Ref: https://leetcode.com/problems/prime-palindrome/discuss/146798/JavaC%2B%2BPython-All-Even-Length-Palindrome-are-Divisible-by-11
# Algo: math

class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        def isPrime(x):
            if x < 2 or x % 2 == 0:
                return x == 2
            for i in xrange(3, int(x ** 0.5) + 1, 2):
                if x % i == 0:
                    return False
            return True
        if 8 <= N <= 11:
            return 11
        for x in xrange(10 ** (len(str(N)) / 2), 10 ** 5):
            y = int(str(x) + str(x)[-2::-1])
            if y >= N and isPrime(y):
                return y

if __name__ == "__main__":
    sol = Solution()
    print sol.primePalindrome(1)

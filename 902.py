# Ref: https://leetcode.com/problems/numbers-at-most-n-given-digit-set/discuss/168279/Python-O(logN)

class Solution(object):
    def atMostNGivenDigitSet(self, digits, n):
        """
        :type digits: List[str]
        :type n: int
        :rtype: int
        """
        N = str(n)
        N_size = len(N)
        res = sum(len(digits) ** i for i in xrange(1, N_size))
        i = 0
        while i < N_size:
            res += sum(c < N[i] for c in digits) * (len(digits) ** (N_size - i - 1))
            if N[i] not in digits:
                break
            i += 1
        return res + (i == N_size)

if __name__ == '__main__':
    sol = Solution()
    print sol.atMostNGivenDigitSet(["1", "4", "9"], 1000000000)

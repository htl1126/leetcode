# Ref: https://leetcode.com/problems/smallest-integer-divisible-by-k/discuss/260852/JavaC%2B%2BPython-O(1)-Space-with-Proves-of-Pigeon-Holes

class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        if K % 2 == 0 or K % 5 == 0:
            return -1
        r = 0
        for n in xrange(1, K + 1):
            r = (r * 10 + 1) % K
            if r == 0:
                return n
        return -1

if __name__ == "__main__":
    sol = Solution()
    print sol.smallestRepunitDivByK(3)

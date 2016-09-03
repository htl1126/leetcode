# ref: https://discuss.leetcode.com/topic/55090/python-with-sorting
# For 1, 2, ..., 25, construct 1001, 2002, 2525 and sort.


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        highDigit = 1
        while highDigit * 10 <= n:
            highDigit *= 10
        higherDigit = highDigit * 10
        withKeys = []
        for i in xrange(1, n + 1):
            key = i
            while key < highDigit:
                key *= 10
            withKeys.append(key * higherDigit + i)
        withKeys.sort()
        return [ki % higherDigit for ki in withKeys]

if __name__ == '__main__':
    sol = Solution()
    print sol.lexicalOrder(25)

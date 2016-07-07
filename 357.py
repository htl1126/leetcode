# ref: https://discuss.leetcode.com/topic/47983/java-dp-o-1-solution


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        table = [10, 81]
        for i in xrange(8, 0, -1):
            table.append(table[-1] * i)
        if n >= 10:
            return sum(table)
        else:
            return sum(table[:n])

if __name__ == '__main__':
    sol = Solution()
    print sol.countNumbersWithUniqueDigits(2)

# ref: https://leetcode.com/discuss/92675/handle-this-question
#              -interview-thinking-process-solution


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        table = [0 for _ in xrange(num + 1)]
        offset = 1
        for i in xrange(1, num + 1):
            if i == offset * 2:
                offset <<= 1
            table[i] = table[i - offset] + 1
        return table

if __name__ == '__main__':
    sol = Solution()
    print sol.countBits(5)

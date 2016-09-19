# ref: https://discuss.leetcode.com/topic/59374/simple-python-java


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        return ['%d:%02d' % (h, m) for h in xrange(12) for m in xrange(60)
                if (bin(h) + bin(m)).count('1') == num]

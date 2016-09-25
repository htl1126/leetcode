# ref: https://discuss.leetcode.com/topic/60398/easy-5-lines-python-ac-solution


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        elif num < 0:
            num += 2 ** 32
        res, dic = '', [chr(ord('0') + i) for i in xrange(10)] + \
            'a b c d e f'.split()
        while num:
            res, num = dic[num % 16] + res, num / 16
        return res

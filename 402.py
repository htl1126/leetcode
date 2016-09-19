# ref: https://discuss.leetcode.com/topic/59380/short-python-one-o-n-and-one
#              -regex


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        out = []
        for d in num:
            while k and out and out[-1] > d:
                out.pop()
                k -= 1
            out.append(d)
        return ''.join(out[:-k or None]).lstrip('0') or '0'

if __name__ == '__main__':
    sol = Solution()
    print sol.removeKdigits('10200', 1)

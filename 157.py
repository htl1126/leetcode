# ref: https://leetcode.com/discuss/75083/python-solution-
#              with-explainations-and-comments

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):


class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        ans = 0
        while n > 0:
            buf4 = ['' for _ in xrange(4)]
            l = read4(buf4)
            if not l:
                return ans
            for i in xrange(min(l, n)):
                buf[ans] = buf4[i]
                ans += 1
                n -= 1
        return ans

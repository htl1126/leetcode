# ref: https://discuss.leetcode.com/topic/8795/my-python-40ms-solution/5

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):


class Solution(object):
    def init(self):
        self.queue = []

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        tmpN = n
        ans = 0
        while tmpN > 0:
            tmpBuf = ['' for _ in xrange(4)]
            read4(tmpBuf)
            self.queue += tmpBuf
            read_len = min(len(self.queue), n - ans)
            for i in xrange(read_len):
                buf[ans + i] = self.queue.pop(0)
            tmpN -= read_len
            ans += read_len
            if read_len < 4:
                break
        return ans

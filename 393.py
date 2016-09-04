class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        n, i = len(data), 0
        while i < n:
            t = data[i]
            sub_s_len = 1
            if t & 128:
                while t & 128:
                    t, sub_s_len = t << 1, sub_s_len + 1
                sub_s_len -= 1
            if sub_s_len > n - i or sub_s_len == 1 and (data[i] & 128):
                return False
            if any(j for j in xrange(i + 1, i + sub_s_len)
                   if (data[j] >> 6) & 3 != 2):
                return False
            i = i + sub_s_len
        return True

if __name__ == '__main__':
    sol = Solution()
    testcase = [[197, 130, 1], [235, 140, 4], [145]]
    for i in xrange(3):
        print i, testcase[i]
        print sol.validUtf8(testcase[i])

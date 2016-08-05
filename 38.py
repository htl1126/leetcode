class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        n -= 1
        ans = '1'
        for i in xrange(n):
            temp = ''
            begin, end = 0, 1
            while 1:
                while end < len(ans) and ans[begin] == ans[end]:
                    end += 1
                temp += str(end - begin) + ans[begin]
                if end >= len(ans):
                    break
                begin = end
                end = begin + 1
            ans = temp[:]
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.countAndSay(6)

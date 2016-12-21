# ref: https://discuss.leetcode.com/topic/69835/simple-python-solution

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i, g_len, ans = 0, len(g), 0
        for i in xrange(len(s)):
            if s[i] >= g[ans]:
                ans += 1
                if ans == g_len:
                    break
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.findContentChildren([1, 2], [1, 2, 3])

# ref: https://discuss.leetcode.com/topic/70736/one-liners

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())

if __name__ == '__main__':
    sol = Solution()
    print sol.countSegments('Hello, my name is John')

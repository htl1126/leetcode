# ref: https://discuss.leetcode.com/topic/68206/easy-python-solution-with
#              -explaination

class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        return str in (2 * str)[1:-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.repeatedSubstringPattern('abab')

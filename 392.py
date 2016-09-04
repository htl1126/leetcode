# ref: https://discuss.leetcode.com/topic/57073/two-pointers-easy-solution-c


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        sp = 0
        for tp in xrange(len(t)):
            if s[sp] == t[tp]:
                sp += 1
                if sp == len(s):
                    return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print sol.isSubsequence('abc', 'ahbgdc')

# ref: https://leetcode.com/discuss/52671/python-solution-with-dictionary


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        l, r = 0, len(num) - 1
        while l <= r:
            if num[l] in d and d[num[l]] == num[r]:
                l, r = l + 1, r - 1
            else:
                return False
        return True

if __name__ == '__main__':
    sol = Solution()
    print sol.isStrobogrammatic('818')

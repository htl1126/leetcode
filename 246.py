# ref: https://leetcode.com/discuss/52671/python-solution-with-dictionary


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dic = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        l, r = 0, len(num) - 1
        while l <= r:
            if num[l] not in dic or dic[num[l]] != num[r]:
                return False
            l += 1
            r -= 1
        return True

if __name__ == '__main__':
    sol = Solution()
    print sol.isStrobogrammatic('818')

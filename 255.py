# ref: https://discuss.leetcode.com/topic/27674/ac-python-o-n-time-o-1-extra
#              -space


class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        lower = -1 << 31
        stack = []
        for x in preorder:
            if x < lower:
                return False
            while stack and x > stack[-1]:
                lower = stack.pop()
            stack.append(x)
        return True

if __name__ == '__main__':
    sol = Solution()
    print sol.verifyPreorder([4, 2, 1, 3, 6, 5, 7])

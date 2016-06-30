# ref: https://leetcode.com/discuss/107662/1-line-ruby-2-lines-python


class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True
        X = min(points)[0] + max(points)[0]
        return {(x, y) for x, y in points} == {(X - x, y) for x, y in points}

if __name__ == '__main__':
    sol = Solution()
    print sol.isReflected([[-16, 1], [16, 1], [16, 1]])

# ref: https://discuss.leetcode.com/topic/55923/o-n-solution-by-counting-corners
#              -with-detailed-explaination
# ref: https://discuss.leetcode.com/topic/56064/python-solution-based-on-hxtang
#              -s-idea
import collections


class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        left = min(x[0] for x in rectangles)
        right = max(x[2] for x in rectangles)
        top = max(x[3]for x in rectangles)
        bottom = min(x[1] for x in rectangles)
        points = collections.defaultdict(int)
        for l, b, r, t in rectangles:
            A, B, C, D = (l, b), (r, b), (r, t), (l, t)
            for p, q in zip((A, B, C, D), (1, 2, 4, 8)):
                if points[p] & q:
                    return False
                points[p] |= q
        for px, py in points:
            if left < px < right or bottom < py < top:
                if points[(px, py)] not in (3, 6, 9, 12, 15):
                    return False
        return True

if __name__ == '__main__':
    sol = Solution()
    print sol.isRectangleCover([[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4],
                                [3, 2, 4, 4]])

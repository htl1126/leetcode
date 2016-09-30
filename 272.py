# ref: https://discuss.leetcode.com/topic/22953/efficient-python


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        def nextpath(path, kid1, kid2):
            if path:
                if kid2(path):
                    path += kid2(path),
                    while kid1(path):
                        path += kid1(path),
                else:
                    kid = path.pop()
                    while path and kid is kid2(path):
                        kid = path.pop()
        # Use PEP8 style def will cause runtime error, still do not know why
        kidleft = lambda path: path[-1].left
        kidright = lambda path: path[-1].right
        path = []
        while root:
            path += root,
            root = root.left if target < root.val else root.right
        # Use PEP8 style def will cause wrong answer, still do not know why
        dist = lambda node: abs(node.val - target)
        path = path[:path.index(min(path, key=dist)) + 1]
        path2 = path[:]
        nextpath(path2, kidleft, kidright)
        vals = []
        for _ in xrange(k):
            if not path2 or path and dist(path[-1]) < dist(path2[-1]):
                vals += path[-1].val,
                nextpath(path, kidright, kidleft)
            else:
                vals += path2[-1].val,
                nextpath(path2, kidleft, kidright)
        return vals

# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root:
            level = [root]
            while level:
                if len(level) > 1:
                    for i in xrange(len(level) - 1):
                        level[i].next = level[i + 1]
                level = [n for node in level for n in (
                    node.left, node.right) if n]

if __name__ == '__main__':
    sol = Solution()
    root = TreeLinkNode(1)
    root.left = TreeLinkNode(2)
    root.right = TreeLinkNode(3)
    root.left.left = TreeLinkNode(4)
    root.left.right = TreeLinkNode(5)
    root.right.right = TreeLinkNode(7)
    print sol.connect(root)

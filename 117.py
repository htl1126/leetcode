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

# Ref: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/389389/Simply-Simple-Python-Solutions-Level-order-traversal-and-O(1)-space-both-approach
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        dummy = Node(-1)
        tmp = dummy
        res = root  # keep the original location of root
        while root:
            while root:
                if root.left:
                    tmp.next = root.left  # also make dummy point to the left most node at next level
                    tmp = tmp.next
                if root.right:
                    tmp.next = root.right
                    tmp = tmp.next
                root = root.next
            root = dummy.next  # make the left most node at next level the new root
            tmp = dummy
            dummy.next = None  # reset "dummy" and "tmp" as pure dummy nodes
        return res

if __name__ == '__main__':
    sol = Solution()
    root = TreeLinkNode(1)
    root.left = TreeLinkNode(2)
    root.right = TreeLinkNode(3)
    root.left.left = TreeLinkNode(4)
    root.left.right = TreeLinkNode(5)
    root.right.right = TreeLinkNode(7)
    print sol.connect(root)

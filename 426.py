# Ref: https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/discuss/169965/Python-Inorder-Transverse

# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        dummy = Node(0, None, None)
        prev = dummy
        stack, node = [], root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            prev.right, node.left, prev = node, prev, node
            node = node.right
        prev.right, dummy.right.left = dummy.right, prev
        return dummy.right

if __name__ == "__main__":
    root = Node(2)
    root.left = Node(1)
    sol = Solution()
    head = sol.treeToDoublyList(root)
    print head.val, head.left.val, head.left.left.val

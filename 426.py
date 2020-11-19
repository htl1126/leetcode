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
        def convert(node):
            if not node:
                return None, None
            left_head, left_tail = convert(node.left)
            right_head, right_tail = convert(node.right)
            node.left = node.right = None
            new_head = new_tail = node
            if left_head:
                left_tail.right = node
                node.left = left_tail
                new_head = left_head
            if right_head:
                right_head.left = node
                node.right = right_head
                new_tail = right_tail
            return new_head, new_tail
        head, tail = convert(root)
        head.left = tail
        tail.right = head
        return head

if __name__ == "__main__":
    root = Node(2)
    root.left = Node(1)
    sol = Solution()
    head = sol.treeToDoublyList(root)
    print head.val, head.left.val, head.left.left.val

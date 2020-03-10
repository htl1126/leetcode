# Ref: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/discuss/154908/Python-easy-solution-using-stack

# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return
        stack = [head]
        prev = Node(0)
        while stack:
            root = stack.pop()
            root.prev = prev
            prev.next = root
            prev = root
            if root.next:
                stack.append(root.next)
            if root.child:
                stack.append(root.child)
                root.child = None
        head.prev = None
        return head

if __name__ == "__main__":
    sol = Solution()
    print sol.flatten(head)

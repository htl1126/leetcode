# Ref: https://leetcode.com/problems/linked-list-in-binary-tree/discuss/524881/Python-Recursive-Solution-O(N-%2B-L)-Time

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(head, root):
            if not head:
                return True
            if not root:
                return False
            return head.val == root.val and (dfs(head.next, root.left) or dfs(head.next, root.right))
        if not head:
            return True
        if not root:
            return False
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

# ref:
# https://discuss.leetcode.com/topic/9305/detail-explain-about-how-morris
#         -traversal-finds-two-incorrect-pointer


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        cur, pre, first, second = root, None, None, None
        while cur:
            if cur.left:
                temp = cur.left
                while temp.right and temp.right != cur:
                    temp = temp.right
                if temp.right:
                    if pre and pre.val > cur.val:
                        if not first:
                            first, second = pre, cur
                        else:
                            second = cur
                    pre = cur
                    temp.right = None
                    cur = cur.right
                else:
                    temp.right = cur
                    cur = cur.left
            else:
                if pre and pre.val > cur.val:
                    if not first:
                        first, second = pre, cur
                    else:
                        second = cur
                pre = cur
                cur = cur.right
        if first and second:
            first.val, second.val = second.val, first.val
        return

# ref: https://discuss.leetcode.com/topic/28180/c-solution-in-4-lines


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def find_max_len(node, parent, curr_len):
            if not node:
                return curr_len
            if parent and parent.val + 1 == node.val:
                curr_len += 1
            else:
                curr_len = 1
            return max(curr_len, find_max_len(node.left, node, curr_len),
                       find_max_len(node.right, node, curr_len))
        return find_max_len(root, None, 0)

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    root.right.left.left = TreeNode(1)
    print sol.longestConsecutive(root)

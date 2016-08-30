# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def build_tree(in_lo, in_hi, post_lo, post_hi):
            if post_lo > post_hi:
                return None
            if post_lo == post_hi:
                return TreeNode(postorder[post_hi])
            root_val = postorder[post_hi]
            root_idx = inorder.index(root_val)
            root = TreeNode(root_val)
            # call recursively with absolute positions
            root.left = build_tree(in_lo, root_idx - 1,
                                   post_lo, post_lo + (root_idx - in_lo) - 1)
            root.right = build_tree(root_idx + 1, in_hi,
                                    post_lo + (root_idx - in_lo), post_hi - 1)
            return root
        return build_tree(0, len(inorder) - 1, 0, len(postorder) - 1)

if __name__ == '__main__':
    sol = Solution()
    root = sol.buildTree([1, 3, 2], [3, 2, 1])
    print root.val
    print root.right.val
    print root.right.left.val

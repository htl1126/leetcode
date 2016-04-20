# ref: https://leetcode.com/discuss/18101/sharing-my-straightforward
#              -recursive-solution


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.build_tree(preorder, inorder, 0, len(preorder) - 1, 0,
                               len(inorder) - 1)

    def build_tree(self, preorder, inorder, pre_start, pre_end, in_start,
                   in_end):
        if pre_start > pre_end:
            return None
        node = TreeNode(preorder[pre_start])
        for i in xrange(in_start, in_end + 1):
            if inorder[i] == node.val:
                pos = i
                break
        node.left = self.build_tree(
            preorder, inorder, pre_start + 1, pre_start + pos - in_start,
            in_start, pos - 1)
        node.right = self.build_tree(
            preorder, inorder, pre_end - (in_end - pos) + 1, pre_end, pos + 1,
            in_end)
        return node

if __name__ == '__main__':
    sol = Solution()
    tree = sol.buildTree([4, 2, 1, 3, 5], [1, 2, 3, 4, 5])
    print tree.val
    print tree.left.val
    print tree.right.val
    print tree.left.left.val
    print tree.left.right.val

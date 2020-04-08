# Ref: https://leetcode.com/problems/delete-nodes-and-return-forest/discuss/328853/JavaC%2B%2BPython-Recursion-Solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        to_delete_set = set(to_delete)
        ans = []
        def helper(root, is_root):
            if not root:
                return None
            root_deleted = root.val in to_delete_set
            if is_root and not root_deleted:
                ans.append(root)
            root.left = helper(root.left, root_deleted)
            root.right = helper(root.right, root_deleted)
            return None if root_deleted else root 
        helper(root, True)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.delNodes(root, to_delete)

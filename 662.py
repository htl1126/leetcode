# Ref: https://leetcode.com/problems/maximum-width-of-binary-tree/discuss/106707/Python-Straightforward-BFS-and-DFS-solutions
# Algo: BFS

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [(root, 0, 0)]
        cur_depth = ans = left = 0
        for node, depth, pos in queue:
            if node:
                queue.append((node.left, depth + 1, pos * 2))
                queue.append((node.right, depth + 1, pos * 2 + 1))
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos
                ans = max(pos - left + 1, ans)
        return ans

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    print sol.widthOfBinaryTree(root)

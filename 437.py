# ref: https://discuss.leetcode.com/topic/64396/easy-recursive
#              -python-7-lines-solution

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        ans, cache = [0], collections.defaultdict(int)
        cache[0] = 1

        def dfs(root, cur_sum):
            if root:
                cur_sum += root.val
                ans[0] += cache[cur_sum - targetSum]
                cache[cur_sum] += 1
                dfs(root.left, cur_sum)
                dfs(root.right, cur_sum)
                cache[cur_sum] -= 1

        dfs(root, 0)
        return ans[0]

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(11)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right.right = TreeNode(1)
    print sol.pathSum(root, 8)

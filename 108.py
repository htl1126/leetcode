# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        half = len(nums) / 2
        if half:
            root = TreeNode(nums[half])
            root.left = self.sortedArrayToBST(nums[:half])
            root.right = self.sortedArrayToBST(nums[half + 1:])
            return root
        if nums:
            return TreeNode(nums[0])
        return None

if __name__ == '__main__':
    sol = Solution()
    print sol.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])

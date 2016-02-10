# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def check_same_tree(p, q):
            if p == None and q == None:
                return True
            elif (p != None and q != None and p.val == q.val
                 and check_same_tree(p.left, q.left) and check_same_tree(p.right, q.right)):
                return True
            else:
                return False
            
        return check_same_tree(p, q)

if __name__ == '__main__':
    sol = Solution()
    root_1 = TreeNode(1)
    root_1.left = TreeNode(2)
    root_2 = TreeNode(1)
    root_2.left = TreeNode(2)
    print sol.isSameTree(root_1, root_2)

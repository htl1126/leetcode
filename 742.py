import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root.left and not root.right:
            return root.val
        graph = collections.defaultdict(list)
        bfs = [root]
        while bfs:
            new_bfs = []
            for node in bfs:
                for child in (node.left, node.right):
                    if child:
                        graph[node.val].append(child.val)
                        graph[child.val].append(node.val)
                        new_bfs.append(child)
            bfs = new_bfs
        bfs = [k]
        seen = set(bfs)
        while True:
            for n in bfs:
                if len(graph[n]) == 1 and n != root.val:
                    return n
            bfs = [y for x in bfs for y in graph[x] if y not in seen]
            seen |= set(bfs)
        
if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    root.left.left.left.left = TreeNode(6)
    print sol.findClosestLeaf(root, 2)

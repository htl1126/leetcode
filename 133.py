# ref: https://leetcode.com/problems/clone-graph/discuss/902767/Python-dfs-recursive-solution-explained

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        mapping = {}
        def dfs(node):
            mapping[node] = Node(node.val)
            for n in node.neighbors:
                if n not in mapping:
                    dfs(n)
                mapping[node].neighbors.append(mapping[n])
        dfs(node)
        return mapping[node]


if __name__ == '__main__':
    sol = Solution()
    print sol.cloneGraph()

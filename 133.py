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
        dic = {None: None}
        def dfs(node):
            if node:
                if node not in dic:
                    dic[node] = Node(node.val)
                for n in node.neighbors:
                    if n not in dic:
                        dfs(n)
                    dic[node].neighbors.append(dic[n])
        dfs(node)
        return dic[node]


if __name__ == '__main__':
    sol = Solution()
    print sol.cloneGraph()

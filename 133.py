# ref: https://leetcode.com/discuss/64740/python-dfs-short-solution


# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution(object):
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None
        if node.label in self.visited:
            return self.visited[node.label]

        clone = UndirectedGraphNode(node.label)
        self.visited[node.label] = clone
        for n in node.neighbors:
            clone.neighbors.append(self.cloneGraph(n))
        return clone

if __name__ == '__main__':
    sol = Solution()
    print sol.cloneGraph()

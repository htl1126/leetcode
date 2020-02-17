# Ref: https://leetcode.com/problems/is-graph-bipartite/discuss/115543/Easy-Python-Solution

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = {}
        def dfs(node):
            for i in graph[node]:
                if i in color:
                    if color[i] == color[node]:
                        return False
                else:
                    color[i] = 1 - color[node]
                    if not dfs(i):
                        return False
            return True
        for i in xrange(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
        return True

if __name__ == "__main__":
    sol = Solution()
    print sol.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]])

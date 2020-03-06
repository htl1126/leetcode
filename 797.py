# Ref: https://leetcode.com/problems/all-paths-from-source-to-target/discuss/118691/C%2B%2BPython-Backtracking

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        dest = len(graph) - 1
        def dfs(node, path):
            if node == dest:
                ans.append(path)
            else:
                for next in graph[node]:
                    dfs(next, path + [next]) 
        dfs(0, [0])
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.allPathsSourceTarget([[1, 2], [3], [3], []])

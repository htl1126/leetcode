# ref: https://discuss.leetcode.com/topic/21737/8-10-lines-union-
#              find-dfs-and-bfs


class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        parent = range(n)

        def find(x):
            return x if parent[x] == x else find(parent[x])
        for e in edges:
            x, y = map(find, e)
            if x == y:
                return False
            parent[x] = y
        return len(edges) == n - 1

if __name__ == '__main__':
    sol = Solution()
    print sol.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])

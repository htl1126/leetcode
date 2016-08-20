# ref: https://discuss.leetcode.com/topic/30572/share-some-thoughts


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        adj = [set() for _ in xrange(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)
        leaves = [i for i in xrange(n) if len(adj[i]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1:
                    new_leaves.append(j)
            leaves = new_leaves
        return leaves

if __name__ == '__main__':
    sol = Solution()
    print sol.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])

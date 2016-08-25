# ref: https://discuss.leetcode.com/topic/29571/compact-python


class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        parent, rank = {}, {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return 0
            if rank[x] < rank[y]:
                x, y = y, x
            parent[y] = x  # attach the forest of small rank to the larger rank
            rank[x] += rank[x] == rank[y]
            return 1
        counts, count = [], 0
        for i, j in positions:
            x = parent[x] = i, j
            rank[x] = 0
            count += 1
            for y in (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j):
                if y in parent:  # if y was processed before, do union operation
                    count -= union(x, y)
            counts.append(count)
        return counts

if __name__ == '__main__':
    sol = Solution()
    print sol.numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]])

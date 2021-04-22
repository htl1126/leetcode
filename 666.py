class Solution:
    def pathSum(self, nums: List[int]) -> int:
        tree, d = [], 0
        for i in range(4):
            tree.append([[-1]] * (2 ** i))
        for n in nums:
            d = max(n // 100, d)
            tree[n // 100 - 1][n % 100 // 10 - 1] = [n % 10]
        for i in range(d - 2, -1, -1):
            for j, n in enumerate(tree[i]):
                if n[0] != -1:
                    t = []
                    for v in (tree[i + 1][2 * j] + tree[i + 1][2 * j + 1]):
                        if v != -1:
                            t.append(n[0] + v)
                    if t:
                        tree[i][j] = t
        return sum(tree[0][0])

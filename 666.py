# Ref: https://leetcode.com/problems/path-sum-iv/discuss/106887/C%2B%2B-Java-Clean-Code

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        tree = [[0] * 8 for _ in range(5)]
        for n in nums:
            d, p, v = n // 100, n % 100 // 10 - 1, n % 10
            tree[d][p] = tree[d - 1][p // 2] + v
        ans = 0
        for i in range(1, 5):
            for j in range(8):
                if i == 4 or tree[i][j] != 0 and tree[i + 1][2 * j] == 0 and tree[i + 1][2 * j + 1] == 0:
                    ans += tree[i][j]
        return ans

# ref: https://leetcode.com/problems/partition-equal-subset-sum/discuss/276278/Python-DP-and-(DFS%2BMemo)


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s, n, memo = sum(nums), len(nums), {0: True}
        if s & 1:
            return False
        nums.sort(reverse=True)
        def dfs(i, x):
            if x not in memo:
                memo[x] = False
                for j in range(i, n):
                    if x >= nums[j] and dfs(j + 1, x - nums[j]):
                        memo[x] = True
                        break
            return memo[x]
        return dfs(0, s >> 1)

if __name__ == '__main__':
    sol = Solution()
    print sol.canPartition([2, 2, 3, 5])

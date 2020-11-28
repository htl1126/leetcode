# Ref: https://leetcode.com/problems/partition-equal-subset-sum/discuss/276278/Python-DP-and-(DFS%2BMemo)

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s, n, memo = sum(nums), len(nums), {0: True}
        if s & 1:
            return False
        nums.sort(reverse=True)
        def dfs(i, x):
            if x not in memo:
                memo[x] = False
                if x > 0:
                    for j in xrange(i, n):
                        if dfs(j + 1, x - nums[j]):
                            memo[x] = True
                            break
            return memo[x]
        return dfs(0, s >> 1)
        
if __name__ == "__main__":
    sol = Solution()
    print sol.canPartition([1, 5, 11, 5])

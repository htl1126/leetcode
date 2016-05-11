# ref: https://leetcode.com/discuss/55666/python-dfs-solution


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in xrange(index, len(nums)):
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res)

if __name__ == '__main__':
    sol = Solution()
    print sol.combinationSum([2, 3, 6, 7], 7)

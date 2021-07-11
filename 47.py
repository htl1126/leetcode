# ref: https://discuss.leetcode.com/topic/32976/9-line-python-solution-with-1-
#              line-to-handle-duplication-beat-99-of-others


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # The process:
        #   Example input: [1, 1, 2]
        #
        #   n = 1
        #   => ans = [[1]]
        #
        #   n = 1
        #   => ans = [[1, 1]], note here we should avoid duplicates
        #
        #   n = 2
        #   => ans = [[2, 1, 1], [1, 2, 1], [1, 1, 2]]
        if len(nums) <= 1:
            return [nums]
        ans = []
        for p in self.permuteUnique(nums[1:]):
            for i in range(len(nums)):
                ans.append(p[:i] + [nums[0]] + p[i:])
                if i < len(p) and nums[0] == p[i]:
                    break
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.permute([1, 1, 2])

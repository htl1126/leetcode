# ref: https://leetcode.com/discuss/18212/my-elegant-recursive
#              -c-solution-with-inline-explanation
# ref: https://discuss.leetcode.com/topic/17277/one-liners-in-python


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        ans = []
        for p in self.permute(nums[1:]):
            for i in range(len(nums)):
                ans.append(p[:i] + [nums[0]] + p[i:])
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.permute([1, 2])

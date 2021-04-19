# ref: https://discuss.leetcode.com/topic/52227/7-liner-in-python-and-follow-up
#              -question


class Solution(object):
    def combinationSum4(self, nums, target):
        nums, combs = sorted(nums), [1] + [0 for _ in range(target)]
        for i in range(target + 1):
            for num in nums:
                if num > i:
                    break
                combs[i] += combs[i - num]
        return combs[-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.combinationSum4([1, 2, 3], 4)

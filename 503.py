# Ref: https://leetcode.com/problems/next-greater-element-ii/discuss/501587/Python-solution-explained
# Algo: stack

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [-1 for _ in xrange(len(nums))]
        stack = []

        for i in xrange(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
        for i in xrange(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack.pop()] = nums[i]
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.nextGreaterElements([1, 2, 1])

# Ref: https://leetcode.com/problems/jump-game/discuss/20907/1-6-lines-O(n)-time-O(1)-space

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach, size = 0, len(nums) - 1
        for i in range(len(nums)):
            if max_reach < i:
                return False
            if max_reach >= size:
                return True
            max_reach = max(max_reach, i + nums[i])

if __name__ == '__main__':
    sol = Solution()
    print sol.canJump([2, 3, 1, 1, 4])

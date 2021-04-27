# Ref: https://leetcode.com/problems/diagonal-traverse-ii/discuss/597794/Python-One-pass

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if len(ans) <= i + j:
                    ans.append([])
                ans[i + j].append(nums[i][j])
        return [a for r in ans for a in reversed(r)]

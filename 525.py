# Ref: https://leetcode.com/problems/contiguous-array/discuss/99655/Python-O(n)-Solution-with-Visual-Explanation

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = count = 0 
        d = {0: -1}
        for i, num in enumerate(nums):
            count += 1 if num else -1
            if count in d:
                max_len = max(max_len, i - d[count])
            else:
                d[count] = i
        return max_len

if __name__ == "__main__":
    sol = Solution()
    print sol.findMaxLength([0, 1, 0])

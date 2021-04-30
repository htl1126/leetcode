# Ref: https://leetcode.com/problems/continuous-subarray-sum/discuss/99566/Simple-Python-(10-lines)-with-Explanation-58ms-O(n)-time-O(k)-space

class Solution(object):
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cum_sum_mod_k = 0
        mods = {0: -1}
        for i, n in enumerate(nums):
            cum_sum_mod_k = (cum_sum_mod_k + n) % k
            if cum_sum_mod_k in mods and i - mods[cum_sum_mod_k] > 1:
                return True
            if cum_sum_mod_k not in mods:
                mods[cum_sum_mod_k] = i
        return False

if __name__ == "__main__":
    sol = Solution()
    print sol.checkSubarraySum([23, 2, 6, 4, 7], 6)

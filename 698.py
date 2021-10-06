# ref: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/146579/Easy-python-28-ms-beats-99.5

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sums = [0] * k
        subsum = sum(nums) // k
        nums.sort(reverse=True)

        def walk(i):
            if i == len(nums):
                return len(set(sums)) == 1
            for j in range(k):
                sums[j] += nums[i]
                if sums[j] <= subsum and walk(i + 1):
                    return True
                sums[j] -= nums[i]
                # The key is, sums[j] == 0 means for all k > j, sum[k] == 0,
                # because this algorithm always fill the previous buckets before trying the next.
                # ref: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/140541/Clear-explanation-easy-to-understand-C++-:-4ms-beat-100/178509
                if sums[j] == 0:
                    break
            return False        

        return walk(0)

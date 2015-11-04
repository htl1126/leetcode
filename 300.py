# The O(nlgn) DP solution
# O(lgn) comes from the trick that the LIS sequence is kept
# And every number in the LIS sequence should be as small as possible

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        LIS = [1]
        LIS_len = 1
        LIS_sequence = [nums[0]]
        for i in xrange(1, len(nums)):
            if nums[i] < LIS_sequence[0]:
                LIS_sequence[0] = nums[i]
                LIS.append(1)
            elif nums[i] > LIS_sequence[-1]:
                LIS_sequence.append(nums[i])
                LIS_len += 1
                LIS.append(LIS_len)
            else:
                if len(LIS_sequence) > 1:
                    low = 0
                    high = LIS_len - 1
                    mid = -1
                    while low <= high:
                        if low + 1 == high:
                            break
                        mid = (low + high) / 2
                        if nums[i] > LIS_sequence[mid]:
                            low = mid
                        else:
                            high = mid
                    LIS_sequence[high] = nums[i]
                    LIS.append(high + 1)
                else:
                    LIS.append(LIS[-1])
        return len(LIS_sequence)

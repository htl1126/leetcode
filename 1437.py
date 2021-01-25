class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if last >= 0 and i - last - 1 < k:
                        return False
                last = i
        return True

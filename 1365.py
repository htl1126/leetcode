class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 102
        for n in nums:
            count[n + 1] += 1
        for i in range(1, 102):
            count[i] += count[i - 1]
        return [count[n] for n in nums]

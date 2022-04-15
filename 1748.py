class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        return sum(i for i in count if count[i] == 1)

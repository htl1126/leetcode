class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(map(lambda x: 10 <= x <= 99 or 1000 <= x <= 9999 or x == 100000, nums))

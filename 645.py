class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_size = len(nums)
        n_set, all_set = set(), set(range(1, nums_size + 1))
        ans = 0
        for i in nums:
            if i in n_set:
                ans = i
            n_set.add(i)
        return [ans, list(all_set - n_set)[0]]


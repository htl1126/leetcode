class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        nums = list(collections.Counter(deck).values())
        if len(nums) == 1 and nums[0] == 1:
            return False
        gcd = nums[0]
        for i in range(len(nums) - 1):
            gcd = get_gcd(gcd, nums[i + 1])
            if gcd == 1:
                return False
        return True

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        nums = dict((i, 0) for i in xrange(1, n + 1))
        d, s = {3: 1, 5: 2}, {1: 'Fizz', 2: 'Buzz', 3: 'FizzBuzz'}
        for num in nums:
            if nums[num] != 3:
                for m in d:
                    i = num * m
                    while i <= n and not (nums[i] & d[m]):
                        nums[i] |= d[m]
                        i *= m
        return [s[nums[i]] if nums[i] else str(i) for i in xrange(1, n + 1)]

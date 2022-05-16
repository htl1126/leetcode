# Ref: https://leetcode.com/problems/sequential-digits/discuss/853592/Python-Solution-using-queue-explained

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        queue = collections.deque(range(1, 10))
        while queue:
            n = queue.popleft()
            if low <= n <= high:
                ans.append(n)
            last_digit = n % 10
            if last_digit < 9:
                queue.append(n * 10 + last_digit + 1)
        return ans

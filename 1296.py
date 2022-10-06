# Ref: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/discuss/470238/JavaC%2B%2BPython-Exactly-Same-as-846.-Hand-of-Straights

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        c = collections.Counter(nums)
        diff = collections.deque()
        last_checked, remain = -1, 0
        for i in sorted(c):
            # remain > c[i]: number of previous values is more than current value
            #   Example: 2, 2, 2, 3, 3
            # remain > 0 and i > last_checked: previous value is not close enough to current value
            #   Example: 2, 2, 4, 4
            if remain > c[i] or remain > 0 and i > last_checked + 1:
                return False
            diff.append(c[i] - remain)
            last_checked, remain = i, c[i]
            # the queue is full and need to modify the current 'remain'
            #   Example: 1, 2, 2, 3, 3, 4
            #   When i == 3 and k == 3, diff == [1, 1, 0] and remain == 2
            #   and then diff becomes [1, 0] and remain becomes 1
            #   since [1, 2, 3] has used one count of 2 and one count of 3
            if len(diff) == k:
                remain -= diff.popleft()
        return remain == 0


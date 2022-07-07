# Ref: https://leetcode.com/problems/fruit-into-baskets/discuss/170740/JavaC%2B%2BPython-Sliding-Window-for-K-Elements

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count, i = {}, 0
        for j, v in enumerate(fruits):
            count[v] = count.get(v, 0) + 1
            # When we have more than two types of fruits,
            # we just increase i by one so j - i + 1 doesn't change.
            # When we find another subarray with larger length,
            # i won't change so j - i + 1 gets updated with a larger value.
            if len(count) > 2:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0:
                    del count[fruits[i]]
                i += 1
        return j - i + 1

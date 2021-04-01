# Ref: https://leetcode.com/problems/reconstruct-original-digits-from-english/discuss/1131046/Python-Linear-solution-using-Counters-explained

class Solution:
    def originalDigits(self, s: str) -> str:
        cnt = collections.Counter(s)
        # order of words does matter
        digits = ["zero", "two", "four", "six", "eight", "one", "three", "five", "seven", "nine"]
        d_map = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
        counters = [collections.Counter(i) for i in digits]
        count = [0] * 10
        for i, counter in enumerate(counters):
            k = min(cnt[x] // counter[x] for x in counter)
            for x in counter:
                counter[x] *= k
            cnt -= counter
            count[d_map[i]] += k
        return "".join(str(i) * count[i] for i in range(10))

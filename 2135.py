# Ref: https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/discuss/1676852/Python3-bitmask

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        start_w_set = set()
        for w in startWords:
            mask = 0
            for c in w:
                mask ^= 1 << (ord(c) - ord('a'))  # build bitmask for each word
            start_w_set.add(mask)

        ans = 0
        for w in targetWords:
            mask = 0
            for c in w:
                mask ^= 1 << (ord(c) - ord('a'))
            for c in w:
                if mask ^ 1 << (ord(c) - ord('a')) in start_w_set:
                    ans += 1
                    break
        return ans

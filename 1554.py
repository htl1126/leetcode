# ref: https://leetcode.com/problems/strings-differ-by-one-character/discuss/801825/Python-Clean-set-%2B-string-hashing-solution-from-O(NM2)-to-O(NM)

class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        n, m = len(dict), len(dict[0])
        hashes = [0] * n
        MOD = 10 ** 11 + 7  # can't use 10 ** 9 + 7
        
        for i in range(n):
            for j in range(m):
                hashes[i] = (26 * hashes[i] + (ord(dict[i][j]) - ord('a'))) % MOD
        
        base = 1
        for j in range(m - 1, -1, -1):        
            seen = set()
            for i in range(n):
                new_h = (hashes[i] - base * (ord(dict[i][j]) - ord('a'))) % MOD
                if new_h in seen:
                    return True
                seen.add(new_h)
            base = 26 * base % MOD
        return False

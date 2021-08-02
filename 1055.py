# Ref: https://leetcode.com/problems/shortest-way-to-form-string/discuss/399353/Python-O(M-%2B-N)-using-hash-table.-Space-O(M).-With-notes.
# Algo: greedy

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        after, indexes = {}, {}
        # indices: inverted index for each char in 'source'
        # after: after[i] stores inverted indexes for chars after source[i]
        #        after[-1] == indices
        for i in range(len(source) - 1, -2, -1):
            after[i] = dict(indexes)  # make a copy of 'indices', not the ref address
            indexes[source[i]] = i  # keep the nearest index of each char
        i, ans = -1, 1
        for c in target:
            if c not in after[-1]:
                return -1
            elif c not in after[i]:
                ans += 1
                i = -1
            i = after[i][c]
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.shortestWay("abc", "abcbc")

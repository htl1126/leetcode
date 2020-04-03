# Ref: https://leetcode.com/problems/shortest-way-to-form-string/discuss/399353/Python-O(M-%2B-N)-using-hash-table.-Space-O(M).-With-notes.
# Algo: greedy

class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        after, indices = {}, {}
        for i in reversed(xrange(-1, len(source))):
            after[i] = dict(indices)  # make a copy of 'indices', not the ref address
            indices[source[i]] = i  # keep the nearest index of each char
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

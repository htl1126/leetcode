# Ref: https://leetcode.com/problems/beautiful-arrangement/discuss/99738/Easy-Python-~230ms

class Solution:
    def countArrangement(self, n: int) -> int:
        def count(i, X):
            if i == 1:
                return 1
            return sum(count(i - 1, X - {x}) for x in X if x % i == 0 or i % x == 0)
        return count(n, set(range(1, n + 1)))

if __name__ == "__main__":
    sol = Solution()
    print(sol.countArrangement(3))

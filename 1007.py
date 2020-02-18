# Ref: https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/discuss/252633/JavaPython-3-one-pass-counting-O(A-%2B-B)

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        from collections import Counter
        same, countA, countB = Counter(), Counter(A), Counter(B)
        for a, b in zip(A, B):
            if a == b:
                same[a] += 1
        for i in xrange(1, 7):
            if countA[i] + countB[i] - same[i] == len(A):
                return min(countA[i], countB[i]) - same[i]
        return -1

if __name__ == "__main__":
    sol = Solution()
    print sol.minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2])

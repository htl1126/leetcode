# Ref: https://leetcode.com/problems/find-the-town-judge/discuss/242938/JavaC%2B%2BPython-Directed-Graph

class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        count = [0 for _ in xrange(N)]
        for i, j in trust:
            count[i - 1] -= 1
            count[j - 1] += 1
        for i in xrange(N):
            if count[i] == N - 1:
                return i + 1
        return -1

if __name__ == "__main__":
    sol = Solution()
    print sol.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]])

# Ref: https://leetcode.com/problems/friend-circles/discuss/101349/Python-Simple-Explanation

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        seen = set()
        def dfs(node):
            for next_node, connected in enumerate(M[node]):
                if next_node not in seen and connected:
                    seen.add(next_node)
                    dfs(next_node)
        ans = 0
        for i in xrange(len(M)):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])

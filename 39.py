class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, n = [], len(candidates)
        candidates.sort()

        def dfs(begin, cur):
            if sum(cur) == target:
                res.append(cur)
            else:
                for i in xrange(begin, n):
                    if sum(cur + [candidates[i]]) <= target:
                        dfs(i, cur + [candidates[i]])
                    else:
                        return
        dfs(0, [])
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.combinationSum([2, 3, 6, 7], 7)

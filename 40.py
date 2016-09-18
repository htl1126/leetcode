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
                i = begin
                while i < n:
                    if sum(cur + [candidates[i]]) <= target:
                        dfs(i + 1, cur + [candidates[i]])
                        i += 1
                        # avoid duplicates
                        while i < n and candidates[i] == candidates[i - 1]:
                            i += 1
                    else:
                        return
        dfs(0, [])
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.combinationSum([10, 1, 2, 7, 6, 1, 5], 8)

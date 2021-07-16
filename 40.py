class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans, size = [], len(candidates)
        def dfs(i, cur_path, cur_sum):
            if cur_sum == target:
                ans.append(cur_path)
            else:
                while i < size:
                    if cur_sum + candidates[i] <= target: # early cut-off for saving time
                        dfs(i + 1, cur_path + [candidates[i]], cur_sum + candidates[i])
                        i += 1
                        # avoid duplicates
                        # for case [1, 1, 1, 2], target = 4, we just want to get one combination
                        # for [1, 1, 1] where the sum is 2
                        while i < size and candidates[i] == candidates[i - 1]:
                            i += 1
                    else:
                        return
        dfs(0, [], 0)
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.combinationSum([10, 1, 2, 7, 6, 1, 5], 8)

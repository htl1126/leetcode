# Ref: https://leetcode.com/problems/jump-game-iv/discuss/502711/Python-Simple-Solution-with-Explanations

import collections

class Solution:
    def minJumps(self, arr: list) -> int:
        dic = collections.defaultdict(list)
        for i, n in enumerate(arr):
            dic[n].append(i)
        pos_met, num_met = set(), set()
        queue = collections.deque([(0, 0)])
        while queue:
            pos, step = queue.popleft()
            if pos == len(arr) - 1:
                return step
            num = arr[pos]
            pos_met.add(pos)
            for p in [pos + 1, pos - 1] + dic[num] * (num not in num_met):
                 if p not in pos_met and 0 <= p < len(arr):
                     queue.append((p, step + 1))
            num_met.add(num)

if __name__ == "__main__":
    sol = Solution()
    print(sol.minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))

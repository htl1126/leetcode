# Ref: https://leetcode.com/problems/optimal-account-balancing/discuss/95355/Concise-9ms-DFS-solution-(detailed-explanation)

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        m = collections.defaultdict(int)
        
        for t in transactions:
            m[t[0]] -= t[2]
            m[t[1]] += t[2]
        
        debt = list(m.values())
        
        def dfs(s):
            while s < len(debt) and debt[s] == 0:
                s += 1
            if s == len(debt):
                return 0
            
            r = float('inf')
            for i in range(s + 1, len(debt)):
                if debt[i] * debt[s] < 0:
                    # settle s with i
                    debt[i] += debt[s]
                    r = min(r, 1 + dfs(s + 1))
                    # backtrack
                    debt[i] -= debt[s]
            return r
        
        return dfs(0)

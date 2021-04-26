# Ref: https://leetcode.com/problems/accounts-merge/discuss/109161/Python-Simple-DFS-with-explanation!!!

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_account_map = collections.defaultdict(list)
        visited = [False] * len(accounts)
        res = []

        # create a map from email accounts to name IDs (0, 1, 2, ...)
        for i, account_lst in enumerate(accounts):
            for j in range(1, len(account_lst)):
                email_account_map[account_lst[j]].append(i)
                
        def dfs(i, emails):
            if not visited[i]:
                visited[i] = True
                for j in range(1, len(accounts[i])):
                    email = accounts[i][j]
                    emails.add(email)
                    for k in email_account_map[email]:
                        dfs(k, emails)
                        
        for i, account in enumerate(accounts):
            if not visited[i]:
                name, emails = account[0], set()
                dfs(i, emails)
                res.append([name] + sorted(emails))
        return res

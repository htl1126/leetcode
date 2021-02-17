# Ref: https://leetcode.com/problems/count-unhappy-friends/discuss/844105/Python-Clean-Solution

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        dic = {}
        for x, y in pairs:
            dic[x] = preferences[x][:preferences[x].index(y)]
            dic[y] = preferences[y][:preferences[y].index(x)]
        ans = 0
        for i in dic:
            for j in dic[i]:
                if i in dic[j]:
                    ans += 1
                    break
        return ans

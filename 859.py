class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if not(len(s) == len(goal) and len(s) >= 2 and len(goal) >= 2):
            return False

        idx = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                idx.append(i)
        if len(idx) == 2 and s[idx[0]] == goal[idx[1]] and s[idx[1]] == goal[idx[0]]:
            return True

        count_s = collections.Counter(s)
        if len(idx) == 0 and any(i >= 2 for i in count_s.values()):
            return True
        
        return False

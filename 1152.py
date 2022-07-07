# Ref: https://leetcode.com/problems/analyze-user-website-visit-pattern/discuss/899805/DETAILED-Easy-to-Follow-Python-Solution-%2B-Clearly-Explained

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        users = defaultdict(list)
        for user, time, site in sorted(zip(username, timestamp, website), key=lambda x: (x[0], x[1])):
            users[user].append(site)
        patterns = collections.Counter()
        for user, sites in users.items():
            patterns.update(collections.Counter(set(itertools.combinations(sites, 3))))
        return max(sorted(patterns), key=patterns.get)

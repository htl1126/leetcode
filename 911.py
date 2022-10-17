# Ref: https://leetcode.com/problems/online-election/discuss/173382/C%2B%2BJavaPython-Binary-Search-in-Times

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leads, self.times, count = [], times, {}
        lead = -1
        for p in persons:
            count[p] = count.get(p, 0) + 1
            if count[p] >= count.get(lead, 0):
                lead = p
            self.leads.append(lead)

    def q(self, t: int) -> int:
        return self.leads[bisect.bisect(self.times, t) - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

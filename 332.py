import collections
# ref: https://discuss.leetcode.com/topic/36370/short-ruby-python-java-c


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []

        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]])

import collections
# ref: https://discuss.leetcode.com/topic/36370/short-ruby-python-java-c


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = collections.defaultdict(list)
        # after the loop, the locations of destinations are sorted reversely
        for a, b in sorted(tickets)[::-1]:
            targets[a].append(b)
        route = []

        # this function traverses the graph nodes in a lexical order
        # and constructs the route from the end
        def visit(airport):
            while targets[airport]:
                # visit locations in accending order and remove it from the map,
                # so the same edge won't be taken for more than once
                next_loc = targets[airport].pop()
                visit(next_loc)
            route.append(airport)
        visit('JFK')
        return route[::-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]])

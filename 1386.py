# Ref: https://leetcode.com/problems/cinema-seat-allocation/discuss/552211/Python-Very-concise-solution-using-hash-map

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = collections.defaultdict(set)
        for i, j in reservedSeats:
            if j in [2, 3, 4, 5]:  # the group occupying [2, 3, 4, 5] is blocked
                seats[i].add(0)
            if j in [4, 5, 6, 7]:  # the group occupying [4, 5, 6, 7] is blocked
                seats[i].add(1)
            if j in [6, 7, 8, 9]:  # the group occupying [6, 7, 8, 9] is blocked
                seats[i].add(2)
        ans = 2 * n
        for i in seats:
            if len(seats[i]) == 3:  # all the possible group locations are blocked
                ans -= 2
            else:
                ans -= 1
        return ans

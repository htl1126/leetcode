class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(map(lambda x: abs(x[0] - x[1]), zip(sorted(seats), sorted(students))))

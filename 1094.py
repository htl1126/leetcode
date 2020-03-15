# Ref: https://leetcode.com/problems/car-pooling/discuss/317610/JavaC%2B%2BPython-Meeting-Rooms-III

class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        for i, v in sorted(x for n, i, j in trips for x in [[i, n], [j, -n]]):
            capacity -= v
            if capacity < 0:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    print sol.carPooling([[3,2,7],[3,7,9],[8,3,9]], 11)

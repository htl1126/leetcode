# Ref: https://leetcode.com/problems/jump-game-iii/discuss/465602/JavaC%2B%2BPython-1-Line-Recursion

class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        if 0 <= start < len(arr) and arr[start] >= 0:
            arr[start] = -arr[start]
            return arr[start] == 0 or self.canReach(arr, start - arr[start]) or self.canReach(arr, start + arr[start])
        return False

if __name__ == "__main__":
    sol = Solution()
    print sol.canReach([4, 2, 3, 0, 3, 1, 2], 5)

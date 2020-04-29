# Ref: https://leetcode.com/problems/degree-of-an-array/discuss/124317/JavaC%2B%2BPython-One-Pass-Solution

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, count, degree, res = {}, {}, 0, 0
        for i, num in enumerate(nums):
            first.setdefault(num, i)
            count[num] = count.get(num, 0) + 1
            if count[num] > degree:
                degree = count[num]
                res = i - first[num] + 1
            elif count[num] == degree:
                res = min(res, i - first[num] + 1)
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.findShortestSubArray([1, 2, 2, 3, 1])

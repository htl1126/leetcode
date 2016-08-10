class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        num_cite = len(citations)
        left, right = 0, num_cite - 1
        while left <= right:
            mid = (left + right) / 2
            if citations[mid] >= num_cite - mid:
                right = mid - 1
            else:
                left = mid + 1
        return num_cite - left

if __name__ == '__main__':
    sol = Solution()
    print sol.hIndex([0, 1, 3, 5, 6])

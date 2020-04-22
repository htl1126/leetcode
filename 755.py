class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        for _ in xrange(V):
            j, lowest = K, heights[K]
            for i in xrange(K, -1, -1):
                if heights[i] < lowest:
                    lowest = heights[i]
                    j = i
                if i - 1 >= 0 and heights[i - 1] > heights[i]:
                    break
            if j != K:
                heights[j] += 1
            else:
                j, lowest = K, heights[K]
                for i in xrange(K, len(heights)):
                    if heights[i] < lowest:
                        lowest = heights[i]
                        j = i
                    if i + 1 < len(heights) and heights[i] < heights[i + 1]:
                        break
                heights[j] += 1
        return heights

if __name__ == "__main__":
    sol = Solution()
    print sol.pourWater([3,1,3], 5, 1)

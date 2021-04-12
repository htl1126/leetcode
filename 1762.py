class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxH = heights[-1]
        ans = [len(heights) - 1]
        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > maxH:
                ans.append(i)
                maxH = heights[i]
        return ans[::-1]

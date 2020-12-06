# Ref: https://leetcode.com/problems/can-place-flowers/discuss/103890/Python-Straightforward-with-Explanation

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i, x in enumerate(flowerbed):
            if (not x and (i == 0 or flowerbed[i - 1] == 0) 
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)):
                n -= 1
                flowerbed[i] = 1
        return n <= 0

if __name__ == "__main__":
    sol = Solution()
    print sol.canPlaceFlowers([1, 0, 0, 0, 1], 1)

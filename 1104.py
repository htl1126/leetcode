# Ref: https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/discuss/323310/Python-1-Line-Solution

class Solution(object):
    def pathInZigZagTree(self, x):
        """
        :type label: int
        :rtype: List[int]
        """
        return self.pathInZigZagTree(3 * 2 ** (len(bin(x)) - 4) - 1 - x / 2) + [x] if x > 1 else [1]
        
if __name__ == "__main__":
    sol = Solution()
    print sol.pathInZigZagTree(14)

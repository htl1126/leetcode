class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")

if __name__ == "__main__":
    sol = Solution()
    print sol.judgeCircle("UD")

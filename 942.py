# Ref: https://leetcode.com/problems/di-string-match/discuss/194904/C%2B%2BJavaPython-Straight-Forward

class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        left = right = 0
        ans = [0]
        for c in S:
            if c == 'I':
                right += 1
                ans.append(right)
            if c == 'D':
                left -= 1
                ans.append(left)
        return [i - left for i in ans]

if __name__ == "__main__":
    sol = Solution()
    print sol.diStringMatch("IDID")

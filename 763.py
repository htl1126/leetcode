# Ref: https://leetcode.com/problems/partition-labels/discuss/298474/Python-two-pointer-solution-with-explanation

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        rightmost = {c: i for i, c in enumerate(S)}
        left, right = 0, 0
        ans = []
        for i, c in enumerate(S):
            right = max(right, rightmost[c])
            if i == right:
                ans.append(right - left + 1)
                left = i + 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.partitionLabels("ababcbacadefegdehijhklij")

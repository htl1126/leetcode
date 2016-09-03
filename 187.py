# ref: https://discuss.leetcode.com/topic/27517/7-lines-simple-java-o-n


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen, repeated = set(), set()
        for i in xrange(len(s) - 9):
            sub_s = s[i:i + 10]
            if sub_s not in seen:
                seen.add(sub_s)
            else:
                repeated.add(sub_s)
        return list(repeated)

if __name__ == '__main__':
    sol = Solution()
    print sol.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')

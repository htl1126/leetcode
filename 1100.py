# Ref: https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/discuss/322928/JavaC%2B%2BPython-Sliding-Window

class Solution(object):
    def numKLenSubstrNoRepeats(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: int
        """
        ans, i = 0, 0
        cur = set()
        for j in xrange(len(S)):
            while S[j] in cur:
                cur.remove(S[i])
                i += 1
            cur.add(S[j])
            ans += j - i + 1 >= K
        return ans
        
if __name__ == "__main__":
    sol = Solution()
    print sol.numKLenSubstrNoRepeats("havefunonleetcode", 5)

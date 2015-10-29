# ad-hoc

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        ans = ''
        minlen = min([len(lst) for lst in strs])
        num_str = len(strs)
        for i in xrange(minlen):
            if [s[i] for s in strs].count(s[i]) == num_str:
                ans = '{0}{1}'.format(ans, strs[0][i])
            else:
                break
        return ans

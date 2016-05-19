# ref: https://leetcode.com/discuss/50163/1-4-lines-ruby-and-python
import collections


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        groups = collections.defaultdict(list)
        for s in strings:
            groups[tuple((ord(c) - ord(s[0])) % 26 for c in s)] += s,
        return map(sorted, groups.values())

if __name__ == '__main__':
    sol = Solution()
    print sol.groupStrings()

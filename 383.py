import collections


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic_note = collections.Counter(ransomNote)
        dic_mg = collections.Counter(magazine)
        return all(dic_note[c] <= dic_mg[c] for c in dic_note)

if __name__ == '__main__':
    sol = Solution()
    print sol.canConstruct('aa', 'ab')

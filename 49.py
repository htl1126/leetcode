class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in dic:
                dic[sorted_str].append(str)
            else:
                dic[sorted_str] = [str]
        return [[str for str in dic[sorted_str]] for sorted_str in dic]

if __name__ == '__main__':
    sol = Solution()
    print sol.groupAnagrams(['ate', 'eat', 'bam', 'amb'])

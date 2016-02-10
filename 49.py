class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        word_dict = {}
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string in word_dict:
                word_dict[sorted_string].append(string)
            else:
                word_dict[sorted_string] = [string]
        result = []
        for string in word_dict:
            result.append(sorted(word_dict[string]))
        return result

if __name__ == '__main__':
    sol = Solution()
    print sol.groupAnagrams(['ate', 'eat', 'bam', 'amb'])

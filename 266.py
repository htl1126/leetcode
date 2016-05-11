class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        freq_lst = freq.values()
        freq_lst = [item % 2 for item in freq_lst]
        if len(s) % 2 == 0:
            if sum(freq_lst)  == 0:
                return True
            else:
                return False
        else:
            if sum(freq_lst) == 1:
                return True
            else:
                return False

if __name__ == '__main__':
    sol = Solution()
    print sol.canPermutePalindrome('carerac')

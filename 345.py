class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowel_set = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        ptr_1, ptr_2 = 0, len(s) - 1
        while 1:
            while ptr_1 < len(s) and s[ptr_1] not in vowel_set:
                ptr_1 += 1
            while ptr_2 >= 0 and s[ptr_2] not in vowel_set:
                ptr_2 -= 1
            if ptr_1 >= ptr_2:
                break
            s[ptr_1], s[ptr_2] = s[ptr_2], s[ptr_1]
            ptr_1 += 1
            ptr_2 -= 1
        return ''.join(s)

if __name__ == '__main__':
    sol = Solution()
    print sol.reverseVowels('xyz')

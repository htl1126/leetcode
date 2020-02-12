class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter = filter(lambda l: l[l.find(' ') + 1].isalpha(), logs)
        digit = filter(lambda l: l[l.find(' ') + 1].isdigit(), logs)
        return sorted(letter, key=lambda x: (x[x.find(' '):], x[:x.find(' ')])) + digit

if __name__ == "__main__":
    sol = Solution()
    print sol.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])

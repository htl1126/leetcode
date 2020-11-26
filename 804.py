class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        table = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
                 "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
                 "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
                 "-.--", "--.."]
        s = set()
        for w in words:
            t = ""
            for c in w:
                t += table[ord(c) - ord('a')]
            s.add(t)
        return len(s)

if __name__ == '__main__':
    sol = Solution()
    print sol.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])

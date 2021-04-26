class Solution:
    def frequencySort(self, s: str) -> str:
        c = collections.Counter(s)
        chrs = list(c.items())
        chrs.sort(key=lambda x: -x[1])
        return ''.join([c * n for c, n in chrs])

if __name__ == '__main__':
    sol = Solution()
    print sol.frequencySort('tree')

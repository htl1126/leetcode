# Ref: https://leetcode.com/problems/open-the-lock/discuss/142561/Python-16-lines-simple-and-readable-BFS-solution-beats-94
# Algo: BFS

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        checked_and_deadend, q, count, move = set(deadends), ["0000"], 0, {str(i): [str((i + 1) % 10), str((i - 1) % 10)] for i in range(10)}
        if "0000" in checked_and_deadend:
            return -1
        while q:
            new = []
            count += 1
            for s in q:
                for i, c in enumerate(s):
                    for cur in (s[:i] + move[c][0] + s[i + 1:], s[:i] + move[c][1] + s[i + 1:]):
                        if cur not in checked_and_deadend:
                            if cur == target:
                                return count
                            checked_and_deadend.add(cur)
                            new.append(cur)
            q = new
        return -1

if __name__ == "__main__":
    sol = Solution()
    print sol.openLock(["0201", "0101", "0102", "1212", "2002"], "0202")

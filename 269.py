# ref: https://discuss.leetcode.com/topic/22476/16-18-lines-python-30-lines-c
import collections


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        pre, suc = collections.defaultdict(set), collections.defaultdict(set)
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    pre[b].add(a)
                    suc[a].add(b)
                    break
        chars = set(''.join(words))
        free = chars - set(pre)
        order = ''
        while free:
            a = free.pop()
            order += a
            for b in suc[a]:
                pre[b].discard(a)
                if not pre[b]:
                    free.add(b)
        return order * (set(order) == chars)

if __name__ == '__main__':
    sol = Solution()
    print sol.alienOrder(["wrt", "wrf", "er", "ett", "rftt"])

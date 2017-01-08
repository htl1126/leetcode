# ref: https://discuss.leetcode.com/topic/65695/python-short-bfs
#              -topological-sort


import collections

class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        if org and not seqs or not org and seqs:
            return False
        edge = collections.defaultdict(set)
        nodes = set(org)
        for seq in seqs:
            n = len(seq)
            if n == 1 and seq[0] not in nodes:
                return False
            for i in xrange(n - 1):
                edge[seq[i]].add(seq[i + 1])
        n = len(org)
        if n == 1:
            return all(seq == org for seq in seqs)
        for i in xrange(n - 1):
            a, b = org[i], org[i + 1]
            if a not in edge or b not in edge[a]:
                return False
            edge.pop(a)
        return not edge

if __name__ == '__main__':
    sol = Solution()
    print sol.sequenceReconstruction([1, 2, 3], [[1, 2], [1, 3], [2, 3]])

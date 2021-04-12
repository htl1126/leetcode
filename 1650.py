# Ref: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/discuss/1081954/Python-O(1)-space-with-drawing-to-explain


"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        curP, curQ = p, q
        while curP != curQ:
            curP = curP.parent if curP.parent else q
            curQ = curQ.parent if curQ.parent else p
        return curP

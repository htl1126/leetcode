# ref: https://leetcode.com/discuss/26815/clear-and-short-python-o-2n-and-o-n
#              -solution
# Similar to 133: Clone Graph
import collections


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = {None: None}
        n = head
        while n:
            if n not in dic:
                dic[n] = Node(n.val)
            if n.next not in dic:
                dic[n.next] = Node(n.next.val)
            dic[n].next = dic[n.next]
            if n.random not in dic:
                dic[n.random] = Node(n.random.val)
            dic[n].random = dic[n.random]
            n = n.next
        return dic[head]

if __name__ == '__main__':
    sol = Solution()
    print sol.copyRandomList()

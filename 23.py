# ref: https://leetcode.com/discuss/55662/108ms-python-solution-with
#              -heapq-and-avoid-changing-heap-size
import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# NOTE: this code must be run with Python not Python3
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = node = ListNode(None)
        h = [(n.val, n) for n in lists if n]
        heapq.heapify(h)
        while h:
            val, n = heapq.heappop(h)
            if n.next:
                heapq.heappush(h, (n.next.val, n.next))
            node.next = n
            node = node.next
        return dummy.next

if __name__ == '__main__':
    sol = Solution()
    head_1 = ListNode(1)
    head_1.next = ListNode(3)
    head_1.next.next = ListNode(5)
    head_2 = ListNode(2)
    head_2.next = ListNode(4)
    head_3 = ListNode(6)
    head_3.next = ListNode(7)
    result = sol.mergeKLists([])
    while result:
        print result.val
        result = result.next

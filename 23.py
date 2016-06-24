# ref: https://leetcode.com/discuss/55662/108ms-python-solution-with
#              -heapq-and-avoid-changing-heap-size


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from heapq import heappop, heapreplace, heapify
        dummy = node = ListNode(None)
        h = [(n.val, n) for n in lists]
        heapify(h)
        while h:
            val, n = h[0]
            if n.next is None:
                heappop(h)
            else:
                heapreplace(h, (n.next.val, n.next))
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
    result = sol.mergeKLists([head_1, head_2, head_3])
    while result:
        print result.val
        result = result.next

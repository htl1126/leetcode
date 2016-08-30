# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev, slow = slow, slow.next
            fast = fast.next.next
        if fast:
            prev, slow = slow, slow.next
        prev.next = None
        # reverse the second half
        p, q = slow, slow.next
        p.next = None
        while q:
            q.next, tmp = p, q.next
            p, q = q, tmp
        half_1, half_2 = head, p
        while half_1.next:
            half_1.next, half_2.next, half_2, half_1 = (
                half_2, half_1.next, half_2.next, half_1.next)
        if half_2:
            half_1.next = half_2

if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1)
    #head.next = ListNode(2)
    #head.next.next = ListNode(3)
    #head.next.next.next = ListNode(4)
    #head.next.next.next.next = ListNode(5)
    sol.reorderList(head)
    #while head:
    #    print head.val
    #    head = head.next

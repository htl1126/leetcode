# ref: https://leetcode.com/discuss/34749/concise-python-code-with-comments
# Alternating the sequences, guaranteed to find the solution within two cycles
# Example
# A: [1 3 4]
# B: [1 2 3 4]
# During running the visiting sequence for each will be
# A: 1 3 4 1 2[3]4 1 2 3...
# B: 1 2 3 4 1[3]4
#              ^ -> found the first intersection here


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        pa = headA
        pb = headB
        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa

if __name__ == '__main__':
    sol = Solution()
    headA = ListNode(1)
    headA.next = ListNode(2)
    headA.next.next = ListNode(3)
    headB = ListNode(2)
    headB.next = headA.next.next
    headA.next.next.next = ListNode(4)
    ptr = sol.getIntersectionNode(headA, headB)
    print ptr.val

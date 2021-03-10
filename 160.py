# ref: https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49846/Python-solution-for-intersection-of-two-singly-linked-lists


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        curA, curB = headA, headB
        lenA, lenB = 0, 0
        while curA:
            curA = curA.next
            lenA += 1
        while curB:
            curB = curB.next
            lenB += 1
        curA, curB = headA, headB
        for _ in range(abs(lenA - lenB)):
            if lenA > lenB:
                curA = curA.next
            else:
                curB = curB.next
        while curA != curB:
            curA, curB = curA.next, curB.next
        return curA

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

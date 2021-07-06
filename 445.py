# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_len, l2_len = self.getLen(l1), self.getLen(l2)
        if l1_len < l2_len:
            l1_len, l2_len = l2_len, l1_len
            l1, l2 = l2, l1
        carry = self.getSum(l1, l2, 0, l1_len - l2_len)
        if carry:
            new_head = ListNode(1)
            new_head.next = l1
            return new_head
        return l1

    def getLen(self, l):
        if l:
            return 1 + self.getLen(l.next)
        return 0

    def getSum(self, l1, l2, cur, size_diff):
        if l1 == None or l2 == None:
            return 0
        if cur >= size_diff:
            carry = self.getSum(l1.next, l2.next, cur + 1, size_diff)
            l1.val += l2.val + carry
        else:
            carry = self.getSum(l1.next, l2, cur + 1, size_diff)
            l1.val += carry
        if l1.val >= 10:
            l1.val -= 10
            return 1
        return 0

if __name__ == "__main__":
    sol = Solution()
    n1 = ListNode(7)
    n1.next = ListNode(2)
    n1.next.next = ListNode(4)
    n1.next.next.next = ListNode(3)
    n2 = ListNode(5)
    n2.next = ListNode(6)
    n2.next.next = ListNode(4)
    ans = sol.addTwoNumbers(n1, n2)
    print ans.val, ans.next.val, ans.next.next.val, ans.next.next.next.val, ans.next.next.next.next == None

# ref: https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11491/Succinct-iterative-Python-O(n)-time-O(1)-space

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
    
        while True:
            count = 0
            while r and count < k:   # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                # connect two k-groups, also make 'dummy' connect to the first new k-group
                jump.next, jump, l = pre, l, r
            else:
                return dummy.next

if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    res = sol.reverseKGroup(None, 2)
    while res:
        print res.val
        res = res.next

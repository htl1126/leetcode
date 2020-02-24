# Ref: https://leetcode.com/problems/add-two-numbers-ii/discuss/202769/Fast-simple-Python

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def get_num(head):
            n = 0
            while head:
                n = n * 10 + head.val
                head = head.next
            return n
        s = get_num(l1) + get_num(l2)
        node_list = list(str(s))
        head = cur = None
        for i, c in enumerate(node_list):
            if i == 0:
                head = cur = ListNode(int(c))
            else:
                cur.next = ListNode(int(c))
                cur = cur.next
        return head

if __name__ == "__main__":
    sol = Solution()
    n1 = ListNode(9)
    n1.next = ListNode(9)
    n2 = ListNode(1)
    ans = sol.addTwoNumbers(n1, n2)
    print ans.val, ans.next.val, ans.next.next.val

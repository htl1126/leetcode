# ref: https://discuss.leetcode.com/topic/17521/share-my-python-solution-with
#              -detailed-explanation


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        try:
            fast = head.next
            slow = head
            while fast is not slow:
                slow = slow.next
                fast = fast.next.next
        except:
            return None
        slow = slow.next
        while head is not slow:
            head = head.next
            slow = slow.next
        return head

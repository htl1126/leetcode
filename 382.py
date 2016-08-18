# ref: https://discuss.leetcode.com/topic/53844/buffered-reservoir-sampling
import random
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        node = self.head
        before = 0
        buffer = [None for _ in xrange(100)]
        while node:
            now = 0
            while node and now < 100:
                buffer[now] = node
                node = node.next
                now += 1
            r = random.randrange(before + now)
            if r < now:
                pick = buffer[r]
            before += now
        return pick.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

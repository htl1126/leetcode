# Ref: https://leetcode.com/problems/my-calendar-i/discuss/109476/Binary-Search-Tree-python

class Node(object):
    def __init__(self, s, e):
        self.s = s
        self.e = e
        self.left = None
        self.right = None

class MyCalendar(object):

    def __init__(self):
        self.root = None

    def helper(self, s, e, node):
        if s >= node.e:
            if node.right:
                return self.helper(s, e, node.right)
            else:
                node.right = Node(s, e)
                return True
        elif e <= node.s:
            if node.left:
                return self.helper(s, e, node.left)
            else:
                node.left = Node(s, e)
                return True
        else:
            return False

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.root:
            self.root = Node(start, end)
            return True
        return self.helper(start, end, self.root)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

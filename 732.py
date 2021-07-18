# ref: https://leetcode.com/problems/my-calendar-iii/discuss/109556/JavaC%2B%2B-Clean-Code
# Solution similar to 1094. Car Pooling

class MyCalendarThree:

    def __init__(self):
        self.time = []

    def book(self, start: int, end: int) -> int:
        bisect.insort(self.time, (start, 1))
        bisect.insort(self.time, (end, -1))
        k, cur_event_count = 0, 0
        for _, i in self.time:
            cur_event_count += i
            k = max(k, cur_event_count)
        return k

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

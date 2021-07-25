# Ref: https://leetcode.com/problems/employee-free-time/discuss/170551/Simple-Python-9-liner-beats-97-(with-explanation)

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = sorted([i for employee in schedule for i in employee], key=lambda x: x.start)
        ans, pre = [], intervals[0]
        for i in intervals[1:]:
            if i.start <= pre.end and i.end > pre.end:
                pre.end = i.end
            elif i.start > pre.end:
                ans.append(Interval(pre.end, i.start))
                pre = i
        return ans

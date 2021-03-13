"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.ans = 0
        data = {employee.id: employee for employee in employees}
        def dfs(i):
            self.ans += data[i].importance
            for j in data[i].subordinates:
                dfs(j)
        dfs(id)
        return self.ans

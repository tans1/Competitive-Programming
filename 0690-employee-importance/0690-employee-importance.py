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
        importances = [0 for _ in range(2001)]
        graph = {}

        for employee in employees:
            graph[employee.id] = employee.subordinates
            importances[employee.id] = employee.importance
        
        self.ans = 0
        def dfs(node, visited):
            visited.add(node)
            self.ans += importances[node]
            for nb in graph[node]:
                if nb not in visited:
                    dfs(nb, visited)
            
            
        
        
        dfs(id, set())
        return self.ans
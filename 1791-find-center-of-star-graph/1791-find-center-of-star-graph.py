class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = {}
        
        for edge in edges:
            i , j = edge
            if i not in graph:
                graph[i] = set()
            if j not in graph:
                graph[j] = set()
            graph[i].add(j)
            graph[j].add(i)
            
        ans = None
        mx = 0
        for k,v in graph.items():
            if len(v) > mx:
                ans = k
                mx = len(v)
        return ans
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        target_mask = (1 << n) - 1  
        
        queue = deque([(i, 1 << i) for i in range(n)])  
        visited = set((i, 1 << i) for i in range(n))  
        steps = 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                node, mask = queue.popleft()
                
                if mask == target_mask:
                    return steps
                
                for neighbor in graph[node]:
                    new_mask = mask | (1 << neighbor)
                    if (neighbor, new_mask) not in visited:
                        visited.add((neighbor, new_mask))
                        queue.append((neighbor, new_mask))
            
            steps += 1
        
        return -1 
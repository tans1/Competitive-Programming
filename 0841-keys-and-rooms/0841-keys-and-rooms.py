class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for i in range(len(rooms)):
            graph[i].extend(rooms[i])
        
        visited = set()
        q = deque()
        q.append(0)
        
        while q:
            nd = q.popleft()
            visited.add(nd)
            
            for nb in graph[nd]:
                if nb not in visited:
                    q.append(nb)
        
        n = len(rooms)
        total_visited = sum(visited)
        
        return total_visited == (n*(n-1)) // 2
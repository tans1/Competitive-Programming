class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        direction = [(-1,0),(1,0),(0,-1),(0,1)]
        def bfs():
            q = deque([(entrance[0],entrance[1],0)])
            visited = set()
            visited.add((entrance[0],entrance[1]))
            while q:
                i,j,dst = q.popleft()
                for l,k in direction:
                    if 0 <= i+l < len(maze) and 0 <= j+k < len(maze[0]):
                        if maze[i+l][j+k] == "." and (i+l,j+k) not in visited:
                            q.append((i+l,j+k,dst+1))
                            visited.add((i+l,j+k))
                    else:
                        if i != entrance[0] or j != entrance[1]:
                            return dst
            return -1
        
        return bfs()
                
                
            
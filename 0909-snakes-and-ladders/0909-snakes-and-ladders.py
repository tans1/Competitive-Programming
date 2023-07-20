class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        m,n = len(board),len(board[0])
        dct = defaultdict(int)
        cnt , alt = 1 , 0
        for i in range(m-1,-1,-1):
            if alt % 2 == 0:
                for j in range(n):
                    dct[cnt] = board[i][j]
                    cnt += 1
                    
            else:
                for j in range(n-1,-1,-1):
                    dct[cnt] = board[i][j]
                    cnt += 1
            alt += 1
            
        q = deque([(1,0)])
        visited = set()
        visited.add(1)
        while q:
            cur , moves = q.popleft()
            if cur == m*n:
                return moves
            for i in range(cur+1, min(cur + 6, m*n) + 1):
                if dct[i] != -1:
                    if dct[i] not in visited:
                        q.append((dct[i],moves+1))
                        visited.add(dct[i])
                elif i not in visited:
                    q.append((i,moves+1))
                    visited.add(i)
                    
        return -1
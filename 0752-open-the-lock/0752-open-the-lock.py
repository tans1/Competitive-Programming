class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        q = deque()
        q.append(("0000",0))
        visited = set()
        visited.add('0000')
        while q:
            nd, step = q.popleft()
            if nd == target:
                return step
            
            
            for i in range(4):
                opt1 = list(nd[:])
                opt2 = list(nd[:])
                if nd[i] == '9':
                    opt1[i] = '0'    
                else:
                    opt1[i] = str(int(nd[i]) + 1 )
                    
                if nd[i] == '0':
                    opt2[i] = '9'
                else:
                    opt2[i] = str(int(nd[i]) - 1 )
                
                option1 = ''.join(opt1)
                option2 = ''.join(opt2)
                
                if option1 not in deadends and option1 not in visited:
                    visited.add(option1)
                    q.append((option1, step + 1))
                    
                if option2 not in deadends and option2 not in visited:
                    visited.add(option2)
                    q.append((option2, step + 1))
        return -1
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
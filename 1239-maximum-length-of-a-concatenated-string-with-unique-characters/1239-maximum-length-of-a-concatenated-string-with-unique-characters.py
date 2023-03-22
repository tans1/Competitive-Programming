class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.ans = 0
        n = len(arr)
        
        def dfs(cur, i):
            self.ans = max(self.ans, len(''.join(cur)))
            if i >= n:
                return
                        
            
            if cur:
                temp = ''.join(cur) + arr[i]
                
                if len(set(temp)) == len(temp):
                    cur.append(arr[i])
                    dfs(cur, i + 1)
                    
                    cur.pop()
                    dfs(cur, i + 1)
                    
                else:
                    dfs(cur, i + 1)
            
            else:
                if len(set(arr[i])) == len(arr[i]):
                    cur.append(arr[i])
                    dfs(cur, i + 1)

                    cur.pop()                
                dfs(cur, i + 1)
        
        dfs([], 0)
        
        return self.ans
            
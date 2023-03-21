class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = set()
        
        def dfs(S,i):
            if i >= len(s):
                res.add(tuple(S))
                return
            
            
            S[i] = S[i].swapcase()
            dfs(S,i+1)
            
            S[i] = S[i].swapcase()
            dfs(S,i+1)


            
        
        S = list(s)
        
        dfs(S,0)
        
        ans = list(map(lambda x : ''.join(list(x)), res))

        return ans
            
            
            
            